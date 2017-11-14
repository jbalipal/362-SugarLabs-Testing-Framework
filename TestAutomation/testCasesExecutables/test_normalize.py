# -*- coding: utf-8 -*-
import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/util')
from normalize import *

def test_normalize():
    uni = unicode(sys.argv[1], "utf-8")
    teststr = normalize_string(uni)
    try:
        teststr == sys.argv[2]
        return "Test Passed!"

    except:
        return "Test Failed! Expected: " + sys.argv[2] + " but was: " + teststr

if __name__ == '__main__':
    test_normalize()
    print(test_normalize())

