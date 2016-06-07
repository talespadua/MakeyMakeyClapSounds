import unittest
from beep_reader_player import create_melody
from beep_reader_player import int_max_value

class CreateMelodyTest(unittest.TestCase):
    """Test create_melody function"""
    def setUp(self):
        """Set up method for tests."""
        self.bits = 16
        self.sampling_rate = 8000
        self.volumes = [0.5,0.8,1.0]
        self.freqs = [440,440,440]
        self.durations = [0.5,0.5,1.0]

    def test_create_melody(self):
        """Test the create melody function in a normal situation"""
        # Create the melody
        melody = create_melody(self.bits,self.sampling_rate,self.volumes,self.freqs,self.durations)
        # The length of the melody in samples should be this
        melody_samples = sum(self.durations) * self.sampling_rate
        # Make sure it actually is
        self.assertEqual(melody_samples,len(melody))

        # Make sure the max volume (int value) is not exceeded
        max_value = int_max_value(self.bits)
        self.assertTrue(max(melody) <= max_value)
