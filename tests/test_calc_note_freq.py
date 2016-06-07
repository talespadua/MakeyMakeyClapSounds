import unittest
from beep_reader_player import calculate_note_freq

class CalculateFreqTest(unittest.TestCase):
    """Test calculate_note_freq function"""

    def test_calc_note_freq(self):
        """Test for calculating note frequency"""
        note = 'A4'
        freq = calculate_note_freq(note)
        self.assertEqual(freq,440.0)
