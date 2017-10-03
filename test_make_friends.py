# put this file and 'friend_input.txt' in the model folder
# run this from terminal with 'python test_make_friends.py test_input.txt'
# first line in file is number of buddies to add as friends

# testing make_friends method from friends module
# only testing valid inputs

import sys
import unittest
import ast

from dbus.mainloop.glib import DBusGMainLoop
from friends import *

# don't know why, but this line makes things work
# it also minimizes all my windows whenever i run the driver
mainloop = DBusGMainLoop(set_as_default=True)

class TestFriends(unittest.TestCase):
    def test_make_friends(self):

        # get name of text file from last command line argument, sys.argv[-1]
        f = open(testCaseFile, "r")

        #convert string from text file into a list
        buddyData = ast.literal_eval(f.readline())
        numBuddies = len(buddyData)

        #print buddyDatat
        #print numBuddies

        buddyList = []
        # create instances of BuddyModel() and store in buddyList
        for x in range(0, numBuddies):
            buddyList.append(BuddyModel())

        # set BuddyModel() attributes from text file
        for x in range(0, numBuddies):
            buddyList[x]._nick = buddyData[x][0]
            buddyList[x]._key = buddyData[x][1]
            buddyList[x]._account = buddyData[x][2]
            buddyList[x]._contact_id = buddyData[x][3]

        # create a Friends instance
        # Friends stores friend list as an attribute called _friends
        myFriends = Friends()

        # loop through buddyList and add buddies to myFriends
        # this creates a FriendBuddyModel from the BuddyModel data
        for buddy in buddyList:
            myFriends.make_friend(buddy)

        # create expected dictionary from text file data
        expectedFriends = {}
        for x in range(0, numBuddies):
            key, value = f.readline().rstrip().split(":")
            friend = eval(value)
            expectedFriends[key] = friend

        f.close()

        # test that keys for both dictionaries are equal
        self.assertListEqual(myFriends._friends.keys(), expectedFriends.keys())

        # test the dictionary contents
        for key in myFriends._friends.keys():
            self.assertEqual(myFriends._friends[key].__dict__, expectedFriends[key].__dict__)


if __name__ == '__main__':
    testCaseFile = sys.argv[-1]
    del sys.argv[1:]
    unittest.main()



