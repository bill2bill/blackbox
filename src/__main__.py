import sys
import board
import adafruit_dht
import serial

if __name__ == "__main__":
    port="/dev/ttyAMA0"
    working_dir="/home/volvo/blackbox"
        
    with serial.Serial(port, baudrate=9600, timeout=1) as module:
        attempts = [0] * 20
        curr_date = '19700101'

        for _ in attempts:  
            try:
                raw = module.readline().decode("ascii")
            except:
                continue
            data = raw.split(',')
            length = len(data)
            
            if length > 0:
                if raw[0:6] == "$GPRMC" and length == 13:
                    curr_time = data[1]
                    curr_date = data[9]

                if raw[0:6] == "$GPGGA" and length == 15:
                    lat = data[2]
                    lat_ind = data[3]
                    lng = data[4]
                    lng_ind = data[5]
                    pos = data[6]
                    sat = data[7]
                    hdop = data[8]
                    alt = data[9]

                if raw[0:6] == "$GPVTG" and length == 10:
                    course = data[1]
                    speed = data[7]

    path = f'{working_dir}/log/measure_{curr_date}.csv'

    try:
        temp = ''
        humidity = ''
        sensor = adafruit_dht.DHT11(board.D17)
        temp = str(sensor.temperature)
        humidity = str(sensor.humidity)
        sensor.exit()
    except:
        pass

    with open(path, 'a+') as file_measure:
        gps_data = ','.join([
            str(f'{curr_date}T{curr_time}'),
            str(curr_date), 
            str(curr_time), 
            str(lat), 
            str(lat_ind), 
            str(lng), 
            str(lng_ind), 
            str(pos), 
            str(sat), 
            str(hdop), 
            str(alt), 
            str(course), 
            str(speed),
        ])
        sensor_data = ','.join([str(temp), str(humidity)])
        output = f'{gps_data},{sensor_data}\n'
        
        file_measure.write(output)