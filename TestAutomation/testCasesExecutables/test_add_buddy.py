import os
import sys
import warnings
from dbus.mainloop.glib import DBusGMainLoop
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')
from neighborhood import *

def test_add_buddy():
    mainloop = DBusGMainLoop(set_as_default=True)
    arguments = sys.argv[1].split(",")
    try:
        actMod = ActivityModel(arguments[0], arguments[1])
        buddy = arguments[2]
        os.chdir('../reports')
        f = open("testOutput.html", "a+")
        actMod.add_buddy(buddy)
        test = (actMod.get_buddies())
    except Exception as exception:
        print(exception)
    try:
        str(test) == sys.argv[2]
        return "Test Passed!"

    except:
        return "Test Failed!"

if __name__ == '__main__':
    test_add_buddy()
    print(test_add_buddy())
