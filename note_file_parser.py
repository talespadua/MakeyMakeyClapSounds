#!/usr/bin/env python

# The custom exception class
class NoteFileParsingException(Exception):
    pass

def note_file_parser(filename):
    # Init notes and durations lists, also volumes
    notes = []
    durations = []
    volumes = []
    # Open file and read contents to string
    with open(filename,'r') as f:
        contents = f.read()
    try:
        # Divide string to blocks which contain 'note:duration'
        blocks = contents.split(',')
        # Split the block into note name, duration, volume
        for item in blocks:
            note, duration, volume = item.split(':')
            notes.append(note)
            # Here we must convert to float, it also automatically
            # gets rid of line breaks at the end of lines in the file
            durations.append(float(duration))
            volumes.append(float(volume))
    except:
        # If something goes wrong
        raise NoteFileParsingException('Error in parsing the note file. Check the format.')
    return notes,durations,volumes

def main():
    filename = 'tests/notefile.txt'
    notes,durations = note_file_parser(filename)
    print(notes)
    print(durations)

if __name__=='__main__':
    main()
