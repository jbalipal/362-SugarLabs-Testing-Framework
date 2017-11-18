import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/intro')
from agepicker import *

def test_age_timestamp():
    SPY = 365 * 24 * 60 * 60
    try:
        
        age_in_seconds = int(sys.argv[1]) * SPY
        BTS = int(time.time() - age_in_seconds)
        ageTS = calculate_age(BTS)
        assert ageTS == int(sys.argv[2])
        return "Test Passed!"
    except Exception: 
        age_in_seconds = int(sys.argv[1]) * SPY
        BTS = int(time.time() - age_in_seconds)
        ageTS = calculate_age(BTS)
        return "Test Failed, Expected: " + str(sys.argv[2]) + "but was: " +str(ageTS)

if __name__ == '__main__':
    test_age_timestamp()
    print(test_age_timestamp())
