import unittest
from beep_reader_player import make_sound
from beep_reader_player import create_melody
import numpy as np
import pygame

class MakeSoundTest(unittest.TestCase):
    """Test make_sound function"""
    def setUp(self):
        """Set up method for tests."""
        self.bits = 16
        self.sampling_rate = 8000
        self.volumes = [0.5,0.8,1.0]
        self.freqs = [440,440,440]
        self.durations = [0.5,0.5,1.0]
        self.channels = 1

    def test_create_sound(self):
        """Test the create melody function in a normal situation"""
        # Initialize pygame mixer
        pygame.mixer.pre_init(self.sampling_rate, -self.bits, self.channels)
        pygame.init()
        # Create the melody
        melody = create_melody(self.bits,self.sampling_rate,self.volumes,self.freqs,self.durations)
        melody = np.array(melody).astype(np.int16)
        # Return the sound based on melody
        sound = make_sound(melody)
        # Make sure the Sound object is created
        self.assertTrue(isinstance(sound,pygame.mixer.Sound))
