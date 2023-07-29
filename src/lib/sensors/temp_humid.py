# class TempHumid:
#     """
#     A class to read the temperature and humidity from a DHT11 module in celcius (°C) and relative humiditiy (RH).

#     ...

#     Methods
#     -------
#     read():
#         Reads the current temperature and humiditiy.
#     """

#     def __init__(self, sensor):
#         """
#         Constructs all the necessary attributes for the file_io object.

#         Parameters
#         ----------
#             sensor : str
#                 Adafruit sensor
#         """
#         self.temp = sensor.temperature
#         self.humidity = sensor.humidity

#     def read(self):
#         """
#         Reads the current temperature and humiditiy.

#         Returns
#         -------
#         str
#         """
#         return ','.join([str(self.temp), str(self.humidity)])