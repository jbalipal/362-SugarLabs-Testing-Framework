import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')
from friends import *

def test_make_friend_int():
    try:
        myFriends = Friends()
        myFriends.make_friend(int(sys.argv[1]))
    except AttributeError:
        return "Test Passed!"
    except:
        return "Test Failed EXPECTED: AttributeError, BUT WAS " + sys.exc_infor()[0]

if __name__ == '__main__':
    result = test_make_friend_int()
    print result

