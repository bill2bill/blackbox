# import serial

# class Aq:
#     """
#     A class to read data from a hacked Ikea AQ sensor. Code inspired from https://github.com/Hypfer/esp8266-vindriktning-particle-sensor.

#     ...

#     Methods
#     -------
#     read():
#         Reads the current air quality readings from AQ sensor.
#     """

#     def __init__(self, device = '/dev/ttyAMA0', timeout = 1, attempts = 5):
#         """
#         Constructs all the necessary attributes for the file_io object.

#         Parameters
#         ----------
#             full_file_path : str
#                 Files full path
#         """
#         self.device = device
#         self.timeout = timeout
#         self.attempts = [0] * attempts

#     def parse(buf):
#         if len(buf) > 6:
#             return (buf[5] << 8) | buf[6]
#         return 0

#     def read(self):
#         """
#         Reads the current air quality readings from AQ sensor.

#         Returns
#         -------
#         float
#         """
#         with serial.Serial(self.device, 9600, timeout = self.timeout) as ser:
#             for _ in self.attempts:
#                 rx_raw = ser.read(64)
#                 if len(rx_raw) > 0:
#                     return self.parse(rx_raw)
                
#             raise Exception('Failed to retrieve pm2.5 data.')