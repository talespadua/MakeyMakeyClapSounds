import unittest
from beep_reader_player import create_note

class CreateNoteTest(unittest.TestCase):
    """Test create_note function"""
    def setUp(self):
        """Set up method for tests."""
        # How many bits
        self.bits = 16
        # Sampling rate
        self.sr = 8000
        # Frequency of the note in Hz
        self.freq = 440
        # Note duration
        self.duration = 1.0
        # Max int value for the chosen bit value
        self.max_value = pow(2,self.bits-1)-1
        # Default volume
        self.volume = 1.0

    def test_create_note(self):
        """Test creating a note"""
        note = create_note(self.bits,self.sr,self.volume,self.freq,self.duration)
        # Max and min values for 16 bit int is +-32767
        self.assertEqual(max(note),self.max_value)
        self.assertEqual(min(note),-self.max_value)
        # Length should be same as sampling rate
        self.assertEqual(len(note),self.sr)

    def test_volume(self):
        """Max volume always between 0 and 1"""
        # Volume less than 0
        volume = -2.0
        note = create_note(self.bits,self.sr,volume,self.freq,self.duration)
        # Make sure values correct
        self.assertEqual(max(note),0.0)
        # Volume over 1
        volume = 12.0
        note = create_note(self.bits,self.sr,volume,self.freq,self.duration)
        # Make sure max value still correct
        self.assertEqual(max(note),self.max_value)
