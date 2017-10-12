# driver for add_friend in friends.py

from dbus.mainloop.glib import DBusGMainLoop
from friends import *

# don't know why, but this line makes things work
# it also minimizes all my windows whenever i run the driver
mainloop = DBusGMainLoop(set_as_default=True)

# FriendBuddyModel instances
friend1 = FriendBuddyModel('One', 'keyOne', 'accountOne', 'idOne')
friend2 = FriendBuddyModel('Two', 'keyTwo', 'accountTwo', 'idTwo')
friend3 = FriendBuddyModel('Three', 'keyThree', 'accountThree', 'idThree')
friend4 = FriendBuddyModel('Four', 'keyFour', 'accountFour', 'idFour')
friend5 = FriendBuddyModel('Five', 'keyFive', 'accountFive', 'idFive')

#print(friend1)
#print(friend1.nick)
#print(friend1.key)
#print(friend1.account)
#print(friend1.contact_id)

friends_to_add = [friend1, friend2, friend3, friend4, friend5]

# create a Friends instance
# Friends stores friend list as an attribute called _friends
myFriends = Friends()

# loop through friends_to_add and add friends to myFriends
for friend in friends_to_add:
    myFriends.make_friend(friend)

# _friends is a dictionary and an attribute in the Friends class
for key, value in myFriends._friends.items():
    print "key: " + key
    print "nick: " + value.nick
    print "account: " + value.account
    print "contact_id: " + value.contact_id + "\n"

# for testing we can use
# self.assertEqual(myFriends._friends, expectedFriends)
# or self.assertDictEqual(myFriends._friends, expectedFriends)
# where expectedFriends is a dictionary

