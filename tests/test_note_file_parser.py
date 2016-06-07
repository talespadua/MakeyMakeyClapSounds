import unittest
from note_file_parser import note_file_parser
from note_file_parser import NoteFileParsingException

class NoteFileParserTest(unittest.TestCase):
    """Tests for note parsing from file"""
    def parse_notes_test(self):
        """Parse notes from a file test"""
        notes,durations,volumes = note_file_parser('tests/notefile.txt')
        self.assertEqual(notes,['C4','D4','E4'])
        self.assertEqual(durations,[1.0,1.0,1.0])
        self.assertEqual(volumes,[0.5,0.5,0.5])

    def raise_error_test(self):
        """Raise an exception in case the note file parsing fails"""
        # assertRaises has the following arguments:
        # 1) the expected exception
        # 2) the tested function
        # 3) all of the arguments passed to the tested function (in this case one)
        self.assertRaises(NoteFileParsingException, note_file_parser, 'tests/notefile_error.txt')
