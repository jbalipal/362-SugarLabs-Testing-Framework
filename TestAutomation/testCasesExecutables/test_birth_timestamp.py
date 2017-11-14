import sys
import warnings
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/intro')
from agepicker import *

def test_birth_timestamp():
    try:
        
        birthTS = calculate_birth_timestamp(int(sys.argv[1]))
        expectedBTS = calculate_birth_timestamp(int(sys.argv[2]))
        assert birthTS == expectedBTS
        return "Test Passed!"
    except Exception: 
        birthTS = calculate_birth_timestamp(int(sys.argv[1]))
        expectedBTS = calculate_birth_timestamp(int(sys.argv[2]))
        return "Test Failed, Expected: " + expectedBTS + "but was: " +str(birthTS)

if __name__ == '__main__':
    test_birth_timestamp()
    print(test_birth_timestamp())
