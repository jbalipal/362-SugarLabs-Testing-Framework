import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/intro')
from agepicker import *

def test_age_timestamp():
    try:
        
        
        expectedBTS = calculate_birth_timestamp(int(sys.argv[1]))
        ageTS = calculate_age(expectedBTS)
        assert ageTS == int(sys.argv[2])
        return "Test Passed!"
    except Exception: 
        expectedBTS = calculate_birth_timestamp(int(sys.argv[1]))
        ageTS = calculate_age(expectedBTS)
        return "Test Failed, Expected: " + str(sys.argv[2]) + "but was: " +str(ageTS)

if __name__ == '__main__':
    test_age_timestamp()
    print(test_age_timestamp())
