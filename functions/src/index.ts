import { error } from 'firebase-functions/logger';
import { onSchedule, ScheduleOptions } from 'firebase-functions/v2/scheduler';
import { initializeApp, App } from 'firebase-admin/app';
import { getFirestore, Firestore } from 'firebase-admin/firestore';
import { getStorage, Storage } from 'firebase-admin/storage';
import { Bucket, File } from '@google-cloud/storage';

import * as moment from 'moment'

import * as Papa from 'papaparse';

const options: ScheduleOptions = {
    schedule: "every 1 hours from 4:00 to 22:00",
    region: "europe-west1",
    memory: "2GiB",
    cpu: 2,
    timeoutSeconds: 60 * 30
}

const app: App = initializeApp();

const collection_files_name: string = 'files'
const collection_measures_name: string = 'measures'
const storage_error_name: string = 'measure_.csv'
const degree_capture = /([0-9]{1,3})([0-9]{2}\.[0-9]{4,})/;

function format_lat_long(raw: string, direction: string) {
    // raw has format ddmm.mmmm
    // degrees: number, minutes: number, seconds: number

    const match = raw.match(degree_capture);
    
    if (!match || match.length < 3) {
        return null
    }

    const degrees = parseInt(match[1])
    const minutes = parseFloat(match[2])

    let dd = degrees + (minutes/60);

    // Don't do anything for N or E
    if (direction == "S" || direction == "W") {
        dd = dd * -1;
    } 

    return dd;
}

exports.ingest = onSchedule(options, async () => {
    const storage: Storage = getStorage(app);
    const firestore: Firestore = getFirestore(app);

    const bucket: Bucket = storage.bucket('volvo_blackbox');
    const collection_files = firestore.collection(collection_files_name);
    const collection_measures = firestore.collection(collection_measures_name);

    const snapshot = await collection_files
        .get()
    const file_status: {[key: string]: string} = snapshot
        .docs
        .map(doc => ({id: doc.id, data: doc.data()}))
        .reduce((agg, doc) => Object.assign(agg, {[doc.id]: doc.data.status}), {});

    const old_file_names: string[] = Object.keys(file_status)
    old_file_names.push(storage_error_name)
    
    const raw_files = await bucket.getFiles({directory: 'log', prefix: 'measure_'})
    const files: File[] = raw_files[0]
    const file_names: string[] = files.map(file => file.name.replace('log/', ''))

    try {
        await firestore.runTransaction(async (trans) => {
            for (let i = 0; i < file_names.length; i++) {
                const name: string = file_names[i]
        
                if (!!old_file_names && !old_file_names.includes(name)) {
                    // File not yet uploaded
                    const data = await files[i].download();
                    const raw = data.toString()
                    const csv: string[][] = Papa.parse<string[]>(raw).data;
                    const len = csv.length
                    const last_row = csv.at(-5)

                    if (len > 6 && last_row && last_row.length > 3 && parseInt(last_row[2]) >= 231100) {
                        // File has got to approx midnight

                        for (let i = 0; i < len; i++) {
                            const row = csv[i]
                            if (row.length == 15) {
                                const date_raw = row[0]
                                const lat_raw = row[3]
                                const lat_dir = row[4]
                                const long_raw = row[5]
                                const long_dir = row[6]
                                const sat = parseInt(row[8])
                                const alt = parseInt(row[10])
                                const speed = parseInt(row[12])
                                const temp = parseInt(row[13])
                                const humidity = parseInt(row[14])

                                const lat = format_lat_long(lat_raw, lat_dir)
                                const long = format_lat_long(long_raw, long_dir)

                                const unix = moment(date_raw.replace('T', '').replace('.', '').slice(0,-2), 'DDMMYYHHmmss').unix()

                                const document = {
                                    date: date_raw,
                                    unix: unix,
                                    lat: lat, 
                                    long: long,
                                    sat: sat,
                                    alt: alt,
                                    speed: speed,
                                    temp: temp,
                                    hum: humidity
                                }
                                const key = date_raw.concat(i.toString())

                                trans.set(collection_measures.doc(key), document);
                            }
                        }

                        trans.set(collection_files.doc(name), {status: 'COMPLETE'});
                    }
                }
            }
        });
      
      } catch (e) {
        error([e])
      }
  });