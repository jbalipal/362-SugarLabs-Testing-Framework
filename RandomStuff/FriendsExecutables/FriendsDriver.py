# driver for Friends component

import sys
import unittest
import ast

from friends import *

class TestFriends(unittest.TestCase):
	def test_empty(self):
		print 'this test is empty'

	def test_make_friend_none(self):
		invalidInput = eval(sys.argv[-1])
		print invalidInput
		# create an instance of Friends
		# Friends stores friend list as an attribute called _friends
		myFriends = Friends()

		print invalidInput
		print type(invalidInput)

		self.assertRaises(AttributeError, myFriends.make_friend, invalidInput) 

if __name__=='__main__':
	# Example: cmd line says 'python test_make_friend_none.py arg1 arg2 ...'
	# sys.argv[0] = 'test_make_friend_none.py'
	# sys.argv[1] = 'arg1'
	# ...

	print sys.argv[-1]
	# print for debugging
	#	print sys.argv
	# print sys.argv[1]

	# input from test_make_friend_none.txt
	# this is a list of inputs for now, we can change this later if needed
	invalidInput = eval(sys.argv[-1])

	del sys.argv[1:]
	unittest.main()
