from dbus.mainloop.glib import DBusGMainLoop
mainloop = DBusGMainLoop(set_as_default=True)
import sys
import warnings
sys.path.append('../Project/src/jarabe/frame')
from clipboard import *
warnings.filterwarnings("ignore")


def test_add_to_clipboard_identicalHash():
     
    args = sys.argv[1].split(",")
    clip =Clipboard()
    res = clip.add_object(args[0],int(args[1]))
    res2 = clip.add_object(args[2],int(args[1]))
    ansstr = str(res2)
    try:
        assert ansstr == sys.argv[2]
        return "Test Passed"
    except:
        return "Test Failed! Expected: " + sys.argv[2] + " but got: " + ansstr




if __name__ == '__main__':
    print(test_add_to_clipboard_identicalHash())
