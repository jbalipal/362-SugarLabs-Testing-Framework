from dbus.mainloop.glib import DBusGMainLoop
mainloop = DBusGMainLoop(set_as_default=True)
import sys
import warnings
sys.path.append('../Project/src/jarabe/frame')
from clipboard import *
warnings.filterwarnings("ignore")


def test_delete_clipboard():
     
    try:
        args = sys.argv[1].split(",")
        clip =Clipboard()
        clip.add_object(args[0],int(args[1])) 
        clip.delete_object(int(args[1]))
        res = clip.get_object(int(args[1]))
        return "Test Failed Expected: " + sys.argv[2]
    except:
        return "Test Passed!"




if __name__ == '__main__':
    print(test_delete_clipboard())
