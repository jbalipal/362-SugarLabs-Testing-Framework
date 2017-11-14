import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')
from friends import *

def test_make_friend_bool(myInput):
    
    myFriends = Friends()

    try:
        myFriends.make_friend(myInput)
    except AttributeError:
        return "Test Passed!"
    except:
        return "Test Failed EXPECTED: TypeError, BUT WAS " + sys.exc_infor()[0]

if __name__== '__main__':
    result = test_make_friend_bool(eval(sys.argv[1]))
    print result
