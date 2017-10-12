# for testing the friends module
# uses pytest
# testing make_friend method
#
# Place this file and conftest.py in the model folder
#
# Test none type objects:
# pytest --cmdInput=None TestFriends.py::test_make_friend_none "-s"
# 
# Test strings:
# pytest --cmdInput='this is my string' TestFriends.py::test_make_friend_string "-s"
#
# Test ints:
# pytest --cmdInput=129 TestFriends.py::test_make_friend_int "-s"


import pytest
import sys

# need to add this line to import from friends
sys.path.append('../Project/src/jarabe/model')
from friends import * 

# test for None input
def test_make_friend_none(cmdInput):
	noneInput = eval(cmdInput)
	print noneInput
	print type(noneInput)
	with pytest.raises(AttributeError):
		myFriends = Friends()
		myFriends.make_friend(cmdInput)

# test for String input 
def test_make_friend_string(cmdInput):
	print cmdInput
	print type(cmdInput)
	with pytest.raises(AttributeError):
		myFriends = Friends()
		myFriends.make_friend(cmdInput)
	
# test for Int input
def test_make_friend_int(cmdInput):
	intInput = int(cmdInput)
	print intInput
	print type(intInput)
	with pytest.raises(AttributeError):
		myFriends = Friends()
		myFriends.make_friend(cmdInput)
