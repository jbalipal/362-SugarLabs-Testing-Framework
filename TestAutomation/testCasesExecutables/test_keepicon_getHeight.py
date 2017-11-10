
import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/journal')
from keepicon import *

def test_keepicon_getHeight():
    try:
        icon = KeepIcon()
        height = icon.do_get_preferred_width()
        assert height[1] == int(sys.argv[2])
        return "Test Passed!"
    except Exception: 
        return "Test Failed, Expected: " + sys.argv[2] + "but was: " +str(height[1])

if __name__ == '__main__':
    result = test_keepicon_getHeight()
    print result
