# put this file and 'friend_input.txt' in the model folder
# run this from terminal with 'python test_make_friends.py friend_input.txt'
# first line in file is number of buddies to add as friends

# testing make_friends method from friends module
# only testing valid inputs

import sys
import unittest

from dbus.mainloop.glib import DBusGMainLoop
from friends import *

# don't know why, but this line makes things work
# it also minimizes all my windows whenever i run the driver
mainloop = DBusGMainLoop(set_as_default=True)

class TestFriends(unittest.TestCase):
    def test_make_friends(self):

        # get name of text file from last command line argument, sys.argv[-1]
        f = open(testCaseFile, "r")

        # first line of file has number of buddies
        numBuddies = f.readline()
        buddyList = []

        # create instances of BuddyModel()
        for x in range(0, int(numBuddies)):
            buddyList.append(BuddyModel())

        # set BuddyModel() attributes from text file
        for x in range(0, int(numBuddies)):
            buddyList[x]._account = f.readline().rstrip()
            buddyList[x]._contact_id = f.readline().rstrip()
            buddyList[x]._nick = f.readline().rstrip()
            buddyList[x]._key = f.readline().rstrip()

        # create a Friends instance
        # Friends stores friend list as an attribute called _friends
        myFriends = Friends()

        # loop through buddyList and add buddies to myFriends
        # this creates a FriendBuddyModel from the BuddyModel data
        for buddy in buddyList:
            myFriends.make_friend(buddy)

        # create expected dictionary from text file data
        expectedFriends = {}
        for x in range(0, int(numBuddies)):
            key, value = f.readline().rstrip().split(":")
            friendValues =  value.split(",")
            testFriend = FriendBuddyModel(friendValues[0], friendValues[1], friendValues[2],
                             friendValues[3])

            expectedFriends[key] = testFriend

        f.close()


        # test that keys for both dictionaries are equal
        self.assertListEqual(myFriends._friends.keys(), expectedFriends.keys())

        for key in myFriends._friends.keys():
            self.assertEqual(myFriends._friends[key].__dict__, expectedFriends[key].__dict__)


if __name__ == '__main__':
    testCaseFile = sys.argv[-1]
    del sys.argv[1:]
    unittest.main()



