# import subprocess

# class Cmd:
#     """
#     A class to interact with the system.

#     ...

#     Methods
#     -------
#     last_line():
#         Executes a linux command, tail -n 1 {path}, to retrieve the last line of a file.
#     ssid():
#         Executes a linux command, iwgetid -r, to retrieve the name of the current network the device is connected to.
#     """

#     def last_line(file_path):
#         """
#         Executes a linux command, tail -n 1 {path}, to retrieve the last line of a file.

#         Parameters
#         ----------
#             file_path : str
#                 Path to file.

#         Returns
#         -------
#         str
#         """

#         try:
#             return subprocess.run(['tail', '-n', '1', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3).stdout.decode('ascii')
#         except Exception as e:
#             raise Exception(f'Failed to last line, {str(e)}')

#     def ssid():
#         """
#         Executes a linux command, iwgetid -r, to retrieve the name of the current network the device is connected to.

#         Returns
#         -------
#         str
#         """

#         try:
#             return subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3).stdout.decode('ascii')
#         except Exception as e:
#             raise Exception(f'Failed to retrieve SSID from subsystem, {str(e)}')