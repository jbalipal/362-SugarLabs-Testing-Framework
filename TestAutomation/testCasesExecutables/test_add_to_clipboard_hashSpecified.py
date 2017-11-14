from dbus.mainloop.glib import DBusGMainLoop
mainloop = DBusGMainLoop(set_as_default=True)
import sys
import warnings
sys.path.append('../Project/src/jarabe/frame')
from clipboard import *
warnings.filterwarnings("ignore")


def test_add_to_clipboard_hashSpecified():
    args = sys.argv[1].split(",")
    clipe =Clipboard()
    numid = clipe.add_object(args[0],int(args[1]))
    try:
        assert str(numid) == sys.argv[2]
        return "Test Passed"
    except:
        return "Test Failed! Expected: " + sys.argv[2] + " but got: " + str(numid)



if __name__ == '__main__':
    test_add_to_clipboard_hashSpecified()
    print(test_add_to_clipboard_hashSpecified())
