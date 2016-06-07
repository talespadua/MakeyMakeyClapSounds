import unittest
from beep_reader_player import int_max_value

class IntMaxTest(unittest.TestCase):
    """Tests for integer max value calculation function"""
    def setUp(self):
        """Set up for int max value tests"""
        self.bits = 16
        self.signed_expected_max = 32767
        self.unsigned_expected_max = 65535

    def test_int_max_value_signed(self):
        """Test signed integer max value calculation"""
        signed = True
        max_value = int_max_value(self.bits,signed)
        self.assertEqual(max_value,self.signed_expected_max)

    def test_int_max_value_unsigned(self):
        """Test unsigned integer max value calculation"""
        signed = False
        max_value = int_max_value(self.bits,signed)
        self.assertEqual(max_value,self.unsigned_expected_max)
