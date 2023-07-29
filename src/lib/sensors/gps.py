# class Gps:
#     """
#     A class to read lat, long & time data from a NEO-6M GPS module.

#     Time is measured too as the Pi 3 B+ does not have a RTC built in.

#     ...

#     Methods
#     -------
#     read():
#         Reads the current lat & long position.
#     time():
#         Reads the current time.
#     """

#     def __init__(self, gps):
#         """
#         Constructs all the necessary attributes for the file_io object.

#         Parameters
#         ----------
#             full_file_path : str
#                 Files full path
#         """

#         attempts = [0] * 100
#         for _ in attempts:  
#             try:
#                 raw = str(gps.readline())
#             except:
#                 break
#             data = raw.split(',')
#             print(raw)
#             length = len(data)
#             if length > 0:
#                 if raw[0:6] == "$GPRMC" and length == 13:
#                     self.curr_time = data[1]
#                     self.curr_date = data[9]

#                 if raw[0:6] == "$GPGGA" and length == 15:
#                     self.lat = data[1]
#                     self.lat_ind = data[2]
#                     self.lng = data[3]
#                     self.lng_ind = data[4]
#                     self.pos = data[5]
#                     self.sat = data[6]
#                     self.hdop = data[7]
#                     self.alt = data[8]

#                 if raw[0:6] == "$GPVTG" and length == 10:
#                     self.course = data[1]
#                     self.speed = data[7]

#     def read(self):
#         """
#         Reads the current lat & long position.

#         Returns
#         -------
#         str
#         """
#         return ','.join([
#             str(self.curr_time), 
#             str(self.curr_date), 
#             str(self.lat), 
#             str(self.lat_ind), 
#             str(self.lng), 
#             str(self.lng_ind), 
#             str(self.pos), 
#             str(self.sat), 
#             str(self.hdop), 
#             str(self.alt), 
#             str(self.course), 
#             str(self.speed),
#         ])
        
#     def today(self):
#         """
#         Reads the current time.

#         Returns
#         -------
#         str
#         """
#         return self.curr_date + 'T' + self.curr_time


# # import serial
# # import pynmea2

# # def parseGPS(str):
# #     if str.find('GGA') > 0:
# #         msg = pynmea2.parse(str)
# #         print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units)

# # serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

# # while True:
# #     str = serialPort.readline()
# #     parseGPS(str)