from dbus.mainloop.glib import DBusGMainLoop
mainloop = DBusGMainLoop(set_as_default=True)
import sys
import warnings
sys.path.append('../Project/src/jarabe/frame')
from clipboard import *
warnings.filterwarnings("ignore")

def test_add_to_clipboard():
    clip =Clipboard()
    numid = clip.add_object(sys.argv[1])
    try:
        assert str(numid) == sys.argv[2]
        return "Test Passed"
    except:
        return "Test Failed! Expected: " + sys.argv[2] + " but got: " + str(numid)



if __name__ == '__main__':
    test_add_to_clipboard()
    print(test_add_to_clipboard())

     
