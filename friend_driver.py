# driver for add_friend in friends.py

from dbus.mainloop.glib import DBusGMainLoop
from friends import *

DBusGMainLoop(set_as_default=True)

friend = FriendBuddyModel('Doug', 'testkey', 'testaccount', 'testid')

print(friend)
print(friend.nick)
print(friend.key)
print(friend.account)
print(friend.contact_id)


