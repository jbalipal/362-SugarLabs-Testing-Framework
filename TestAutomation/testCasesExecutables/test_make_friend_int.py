import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')
from friends import *

def test_make_friend_int():
    #os.chdir('../reports')
    #f = open("testOutput.html", "a+")
    try:
        myFriends = Friends()
        myFriends.make_friend(int(sys.argv[1]))
    except AttributeError:
        #print("TEST PASSED")
        #f.write("test_make_friend_int(): TEST PASSED")
        return "test_make_friend_int(): TEST PASSED"
    except:
        #print("TEST FAILED, EXPECTED AttributeError, BUT WAS " + sys.exc_infor()[0])
        #f.write("test_make_friend_int(): TEST FAILED")
        return "test_make_friend_int(): TEST FAILED"

if __name__ == '__main__':
    #print sys.argv[1]
    result = test_make_friend_int()
    print result

