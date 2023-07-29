# import json

# class Logger:
#     """
#     A class to log information on the application as it's executed.

#     ...

#     Methods
#     -------
#     measure(lat, long, temp, humid, aq):
#         Logs information to the logs directory, with level = info, component = measure.
#     info(caller, msg):
#         Logs information to the logs directory, with level = info, component = logger.
#     error(caller, msg):
#         Logs errors to the logs directory, with level = error, component = logger.
#     """

#     def __init__(self, file_measure, time):
#         """
#         Constructs all the necessary attributes for the Logger object.

#         Parameters
#         ----------
#             file : Object
#                 File object to append to a file.
#         """
#         # self.file_log = file_log
#         self.file_measure = file_measure
#         self.time = time

#     def format(self, **kwargs):
#         """
#         Converts a Dict to a JSON object.

#         Parameters
#         ----------
#             kwargs : Dict
#                 all the dimensions to be converted into a JSON.

#         Returns
#         -------
#         str
#         """
#         if kwargs:
#             try:
#                 return json.dumps(kwargs) + '\n'
#             except:
#                 pass
#                 # ignore any exceptions and just return an empty JSON.
#                 # self.error('logger.format', 'Failed to convert kwargs to JSON.')

#         return '{\}'

#     def measure(self, lat, lat_indicator, long, long_indicator, satellites, hdop, altitude, temp, speed, humid):
#         """
#         Logs information to the logs directory, with level = info, component = measure.

#         Parameters
#         ----------
#             lat : float
#                 Latitude.
#             long : float
#                 Longitude.
#             temp : float
#                 Temperature.
#             humid : float
#                 Humidity.
#             aq : float
#                 Air Quality.

#         Returns
#         -------
#         void
#         """

#         try:
#             output = self.format(**{
#                 'level': 'INFO', 
#                 'component': 'measure', 
#                 'caller': 'systemctl',
#                 'ts': self.time,
#                 'lat': str(lat),
#                 'lat_indicator': str(lat_indicator),
#                 'long': str(long),
#                 'long_indicator': str(long_indicator),
#                 'satellites': str(satellites),
#                 'hdop': str(hdop),
#                 'altitude': str(altitude),
#                 'speed': str(speed),
#                 'temp': str(temp),
#                 'humid': str(humid)
#                 # 'aq': str(aq)
#             })
        
#             self.file_measure.write(output)
#         except:
#             # self.error('logger.measure', 'Failed to write INFO logs to file.')
#             pass

#     # def info(self, caller, msg):
#     #     """
#     #     Logs information to the logs directory, with level = info, component = logger.

#     #     Parameters
#     #     ----------
#     #         caller : str
#     #             The method and class where the log occured.
#     #         msg : str
#     #             Message describing the log.

#     #     Returns
#     #     -------
#     #     void
#     #     """

#     #     output = self.format(**{
#     #         'level': 'INFO', 
#     #         'component': 'logger', 
#     #         'caller': caller,
#     #         'ts': self.time,
#     #         'msg': msg,
#     #     })

#     #     try:
#     #         self.file_log.write(output)
#     #     except:
#     #         self.error('logger.info', 'Failed to write INFO logs to file.')

#     # def error(self, caller, msg):
#     #     """
#     #     Logs errors to the logs directory, with level = error, component = logger.

#     #     Parameters
#     #     ----------
#     #         caller : str
#     #             The method and class where the log occured.
#     #         msg : str
#     #             Message describing the log.

#     #     Returns
#     #     -------
#     #     void
#     #     """

#     #     output = self.format(**{
#     #         'level': 'ERROR', 
#     #         'component': 'logger', 
#     #         'caller': caller,
#     #         'ts': self.time,
#     #         'msg': msg,
#     #     })

#     #     try:
#     #         self.file_log.write(output)
#     #     except:
#     #         # If the file write fails an Error cannot be logged
#     #         pass