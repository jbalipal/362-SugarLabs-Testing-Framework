# -*- coding: utf-8 -*-
import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/util')
from normalize import *

def test_normalize_passive():
    #uni = unicode(sys.argv[1], "utf-8")
    #teststr = normalize_string(uni)
    try:
        uni = unicode(sys.argv[1], "utf-8")
        teststr = normalize_string(uni)
        teststr == sys.argv[2]
        return "Test Passed!"
    except ValueError:
        return "Test Failed! Expected: " + sys.argv[2] + " but was: ValueError"

    except:
        return "Test Failed! Expected: " + sys.argv[2] + " but was: " + teststr


if __name__ == '__main__':
    test_normalize_passive()
    print(test_normalize_passive())

