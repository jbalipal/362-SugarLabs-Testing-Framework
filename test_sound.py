# testing sound.py

import unittest
from sound import PlaybackSound

class TestSound(unittest.TestCase):

	def test_get_volume(self):
		# instances of PlaybackSound()
		sound_1 = PlaybackSound()
		sound_2 = PlaybackSound()
		sound_3 = PlaybackSound()
		sound_4 = PlaybackSound()
		sound_5 = PlaybackSound()
		sound_6 = PlaybackSound()

		# set volume for PlaybackSound() instance
		sound_1._volume.set_volume(25)
		self.assertEqual(sound_1.get_volume(), 25)

		# edge cases
		sound_2._volume.set_volume(0)
		self.assertEqual(sound_2.get_volume(), 0)

		sound_3._volume.set_volume(100)
		self.assertEqual(sound_3.get_volume(), 100)

		# negative volume will set to lowest volume, 0
		sound_4.set_volume(-20)
		self.assertEqual(sound_4.get_volume(), 0)
	
		# values greater than 100 will set to max volume, 100
		sound_5.set_volume(1500)
		self.assertEqual(sound_5.get_volume(), 100)

		# test for string input
		self.assertRaises(TypeError, sound_6.get_volume(), 'a string')

