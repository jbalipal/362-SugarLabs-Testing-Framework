import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/intro')
from agepicker import *
import time
import math

def test_birth_timestamp():
    SPY = 365 * 24 * 60 * 60
    try:
        
        age_in_seconds = int(sys.argv[2]) * SPY
        expectedBTS = int(time.time() - age_in_seconds)
        birthTS = calculate_birth_timestamp(int(sys.argv[1]))
        assert birthTS == expectedBTS
        return "Test Passed!"
    except Exception: 
        age_in_seconds = int(sys.argv[2]) * SPY
        expectedBTS = int(time.time() - age_in_seconds)
        birthTS = calculate_birth_timestamp(int(sys.argv[1]))
        AISinput = time.time() - birthTS
        ageinput = int(math.floor(AISinput / SPY) + 0.5)
        AISexpected = time.time() - expectedBTS
        ageexpected = int(math.floor(AISexpected / SPY) + 0.5)
        return "Test Failed, Expected: " + str(ageexpected) + "but was: " + str(ageinput)

if __name__ == '__main__':
    test_birth_timestamp()
    print(test_birth_timestamp())
