const {onSchedule} = require("firebase-functions/v2/scheduler");

import { initializeApp, App } from 'firebase-admin/app';
import { getFirestore, Firestore } from 'firebase-admin/firestore';
import { getStorage, Storage } from 'firebase-admin/storage';
import { Bucket, File } from '@google-cloud/storage';

import * as moment from 'moment'

import * as Papa from 'papaparse';

const app: App = initializeApp();

const collection_files_name: string = 'files'
const collection_measures_name: string = 'measures'
// const collection_loc_name: string = 'loc'

function format_lat_long(raw: string, direction: string) {
    // degrees: number, minutes: number, seconds: number
    const degrees = parseInt(raw.substring(2))
    const minutes = parseInt(raw.substring(2))
    const seconds = parseInt(raw.substring(2))
    let dd = degrees + minutes/60 + seconds/(60*60);

    if (direction == "S" || direction == "W") {
        dd = dd * -1;
    } // Don't do anything for N or E
    return dd;
}

// function transform_header(header: string, index: number) {
// }

exports.accountcleanup = onSchedule("every day 01:00", async () => {
    const storage: Storage = getStorage(app);
    const firestore: Firestore = getFirestore(app);

    const bucket: Bucket = storage.bucket('volvo_blackbox');
    const collection_files = firestore.collection(collection_files_name);
    const collection_measures = firestore.collection(collection_measures_name);
    // const collection_loc = firestore.collection(collection_loc_name);

    const snapshot = await collection_files
        .get()
    const file_status: {[key: string]: string} = snapshot
        .docs
        .map(doc => ({id: doc.id, data: doc.data()}))
        .reduce((agg, doc) => Object.assign(agg, {[doc.id]: doc.data.status}), {});

    const file_names: string[] = Object.keys(file_status)
    
    const files: File[] = await bucket.getFiles()

    try {
        await firestore.runTransaction(async (trans) => {
            for (let i = 0; i < files.length; i++) {
                const file: File = files[i]
                const name: string = file.name
                const doc_file = collection_files.doc(name)
        
                if (!file_names.includes(name)) {
                    // File not yet uploaded
                    const data = await file.download();
                    const raw = data.toString()
                    // const options = {header: true, transformHeader: transform_header}
                    const csv: string[][] = Papa.parse<string[]>(raw).data;
                    const len = csv.length

                    if (len > 900) {
                        // File has got to approx midnight
                        
                        for (let i = 0; i < len; i++) {
                            const row = csv[i]

                            const date_raw = row[0]
                            const lat_raw = row[3]
                            const lat_dir = row[4]
                            const long_raw = row[5]
                            const long_dir = row[6]
                            const sat = row[8]
                            const alt = row[10]
                            const speed = row[12]
                            const temp = row[13]
                            const humidity = row[14]

                            const lat = format_lat_long(lat_raw, lat_dir)
                            const long = format_lat_long(long_raw, long_dir)

                            const date = moment(date_raw.replace("T", ""), "ddMMyyyyHHmmss").unix()

                            const document = {
                                date: date,
                                lat: lat, 
                                long: long,
                                sat: sat,
                                alt: alt,
                                speed: speed,
                                temp: temp,
                                hum: humidity
                            }

                            trans.set(collection_measures.doc(), document);
                        }
                        trans.set(doc_file, {status: 'COMPLETE'});
                    }
                }
            }
        });
      
        console.log('Transaction success!');
      } catch (e) {
        console.log('Transaction failure:', e);
      }
  });