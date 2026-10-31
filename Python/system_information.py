import platform
import getpass
from datetime import datetime

# IT Support Toolkit
# System Information Script

print("================================")
print("     IT SUPPORT TOOLKIT")
print("================================")

print("Computer Name:", platform.node())
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Machine Type:", platform.machine())
print("Python Version:", platform.python_version())
print("Current User:", getpass.getuser())
print("Date and Time:", datetime.now())

print("================================")
print("System information collected!")
