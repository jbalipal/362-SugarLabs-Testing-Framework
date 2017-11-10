
import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/journal')
from keepicon import *

def test_keepicon_getWidth():
    try:
        icon = KeepIcon()
        width = icon.do_get_preferred_width()
        assert width[1] == int(sys.argv[2])
        return "Test Passed!"
    except Exception: 
        return "Test Failed, Expected: " + sys.argv[2] + "but was: " +str(width[1])

if __name__ == '__main__':
    result = test_keepicon_getWidth()
    print result

