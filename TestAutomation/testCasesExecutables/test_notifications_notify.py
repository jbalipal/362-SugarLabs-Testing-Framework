import sys
import warnings
from notifications import NotificationService
#from dbus.mainloop.glib import DBusGMainLoop
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')

def test_notifications_notify():
 #   mainloop = DBusGMainLoop(set_as_default=True)
    arguments = sys.argv[1].split(",")
    try:
        note = Notify(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4], arguments[5], arguments[6], arguments[7])
        print(note)
        os.chdir('../reports')
        f = open("testOutput.html", "a+")
    except Exception as exception:
        print(exception)
    try:
        str(test) == sys.argv[2]
        return "Test Passed!"

    except:
        return "Test Failed!"

if __name__ == '__main__':
    test_notifications_notify()
    print(test_notifications_notify())
