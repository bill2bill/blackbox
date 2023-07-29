import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

def parse(buf):
    if len(buf) > 4:
        return str((buf[5] << 8) | buf[6])
    return '0'

while True:
    rx_raw = ser.read(64)

    if len(rx_raw) > 0:
        print(rx_raw)
        print(parse(rx_raw))