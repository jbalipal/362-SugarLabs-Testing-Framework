#!/usr/bin/python

import os

# something like this would be built by the parser
stringTestCommand = 'pytest --cmdInput="this is my string" TestFriends.py::test_make_friend_string "-s"'
noneTestCommand = 'pytest --cmdInput=None TestFriends.py::test_make_friend_none "-s"'
intTestCommand = 'pytest --cmdInput=147 TestFriends.py::test_make_friend_int "-s"'

testsToExecute = [stringTestCommand, noneTestCommand, intTestCommand]

for test in testsToExecute:
	os.system(test)

