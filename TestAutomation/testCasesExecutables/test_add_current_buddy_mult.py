import os
import sys
import warnings
from dbus.mainloop.glib import DBusGMainLoop
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')
from neighborhood import *

def test_add_current_buddy_mult():
    mainloop = DBusGMainLoop(set_as_default=True)
    arguments = sys.argv[1].split(",")
    try:
        actMod = ActivityModel(arguments[0], arguments[1])
        buddy1 = arguments[2]
        buddy2 = arguments[3]
        os.chdir('../reports')
        f = open("testOutput.html", "a+")
        actMod.add_current_buddy(buddy1)
        actMod.add_current_buddy(buddy2)
        test = (actMod.get_current_buddies())
    except Exception as exception:
        print(exception)
    try:
        str(test) == sys.argv[2]
        return "Test Passed!"

    except:
        return "Test Failed!"

if __name__ == '__main__':
    test_add_current_buddy_mult()
    print(test_add_current_buddy_mult())
