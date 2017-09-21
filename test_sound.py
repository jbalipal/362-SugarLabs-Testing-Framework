# testing sound.py

import unittest
from sound import PlaybackSound

class TestSound(unittest.TestCase):

	def test_get_volume(self):
		sound_1 = PlaybackSound()
		sound_1.set_volume(50)

		self.assertEqual(sound_1.get_volume(), 50)
