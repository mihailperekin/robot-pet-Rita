import getpass
USER_NAME = getpass.getuser()
import os

def add_to_startup(file_path="C:\\coding\\cat\\emotions\\emotions.py"):
    if file_path == "C:\\coding\\cat\\emotions\\emotions.py":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "C:\\coding\\cat\\emotions\\emotions.py" %s' % file_path)
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + 'C:\\coding\\cat\\emotions\\emotions.py' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)