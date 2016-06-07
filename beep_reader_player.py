#!/usr/bin/env/python

import pygame
import numpy as np

from note_file_parser import note_file_parser

class NoteFileParsingException(Exception):
    pass

def int_max_value(bits,signed=True):
    """Returns the maximum int value of a signed or unsigned integer
    based on used bits.
    Arguments:
    bits -- How many bits, e.g., 16
    signed -- True if a signed int
    Returns:
    max_value -- The maximum int value based on given parameters
    """
    if signed:
        # Signed int
        max_value = pow(2,bits-1)-1
    else:
        # Unsigned int
        max_value = pow(2,bits)-1
    return max_value

# Add the data points to an array (create the wave)
def create_note(bits,sampling_rate,volume,freq,duration):
    """Creates a single note as a sine wave.
    Arguments:
    bits -- How many bits are used in the values, e.g., 16
    sampling_rate -- How many samples per second, e.g., 44100
    volume -- Volume, from 0 to 1 (max)
    freq -- The frequency of the note
    duration -- Duration of the note in seconds
    Returns:
    snd_array -- A list of sine wave values based on the current note
    """
    # Make sure volume between 0 and 1
    # The max int value will be multiplied by this
    if volume<0.0: volume = 0.0
    if volume>1.0: volume = 1.0
    # Calculate the maximum int value based on the used bit value (signed int)
    # Basically: what is the maximum signed int value for the amount of bits selected
    max_value = int_max_value(bits)
    # An empty list
    note = []
    duration = float(duration)
    # Fill the list with sine wave values
    for x in range(0, int(sampling_rate*duration)):
        value = volume * max_value * np.sin(2 * np.pi * freq * x / sampling_rate)
        note.append(value)
    return note

def create_melody(bits,sampling_rate,volumes,freqs,durations):
    """Creates and returns a melody consisting of one or more notes.
    Arguments:
    bits -- How many bits are used in the values, e.g., 16
    sampling_rate -- How many samples per second, e.g., 44100
    volumes -- A list of volumes for individual notes
    freqs -- A list of frequencies for individual notes
    durations -- Note durations in a list
    Returns:
    melody -- A list of wave values based on the current melody
    """
    melody = []
    # Go through the list

    # Create an individual note
    note = create_note(bits,sampling_rate,volumes,freqs,durations)
    # Add a note to the melody list
    melody.extend(note)
    return melody

def calculate_note_freq(note):
    """Calculates the frequency of a give note based on it's name and frequency of A4=440Hz.
    All notes and octaves are supported. Not case sensitive.
    Arguments:
    note -- The note name and octave, e.g., 'C4' (string)
    Returns:
    The frequency of the given note
    """
    # The name of the note, e.g., 'A'
    note_name = note[0].upper()
    # The octave of the note, e.g., 4
    note_octave = int(note[1])
    # The note name list
    notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    # The index of A in the list
    baseind = 9
    # The index of the note in the list
    noteind = notes.index(note_name)
    # The index difference (how many semitones difference from A)
    n = noteind - baseind
    # Take into account the octave (relative to A4, that's why we have 4 here)
    # Now n is the number of semitones difference from the note and A4
    n = n + (4-note_octave)*12
    # Approximately 2^(1/12)
    a = 1.059463094359
    # Frequency of A4
    f0 = 440
    # The frequency calculation
    freq = f0 * pow(a,n)
    return freq

def make_sound(melody):
    """Returns pygame sndarray sound.
    Arguments:
    melody - The whole melody as int values as a numpy array
    Returns:
    sound - x
    """
    # Get the sound based on the array
    sound = pygame.sndarray.make_sound(melody)
    return sound

def play_song(sampling_rate,bits,channels,filename):
    """Plays the song based on some parameters and the notefile.
    Arguments:
    sampling_rate - The sampling rate, e.g., 44100 (int)
    bits - Bitrate, e.g., 16 (int)
    channels - How many channels, e.g., 1 (mono) (int)
    filename - The name of the notefile to be parsed (string)
    """
    pygame.init()
    new_round = True

    # screen size
    screen_width = 300
    screen_height = 300

    score_font = pygame.font.SysFont(None, 50)
    text_font = pygame.font.SysFont(None, 25)

    running = True

    game_display = pygame.display.set_mode((screen_width, screen_height))

    while()

    with open(filename, 'r') as f:
        contents = f.read()
    # Divide string to blocks which contain 'note:duration'
    blocks = contents.split(',')
    # Split the block into note name, duration, volume
    for item in blocks:
        note, duration, volume = item.split(':')
        # Here we must convert to float, it also automatically
        # gets rid of line breaks at the end of lines in the file

        # The duration this program is alive, right now the same as note duration
        wait_duration = duration
        # Note frequencies
        freqs = calculate_note_freq(note)

        # Initialize pygame mixer
        pygame.mixer.pre_init(sampling_rate, -bits, channels)
        pygame.init()

        # Create the wave
        melody = create_melody(bits,sampling_rate,volume,freqs,duration)
        # Create a numpy array of the list, needed later.
        # Note: We don't create a numpy array earlier, because when
        # appending values to it, a new array is always created.
        # That is not efficient.
        # Also, in this phase the whole array is converted to integers.
        # Floats cannot be used for pygame sndarray.
        melody = np.array(melody).astype(np.int16)
        # Create the sound
        sound = make_sound(melody)
        # Play and loop
        sound.play()
        # Stop after <duration>
        wait_duration = float(wait_duration)
        pygame.time.delay(int(wait_duration*1000))
        # Stop playing
        sound.stop()
    # If something goes wrong


def main():
    # Set some variables
    sampling_rate = 8000
    bits = 16
    # In this case: mono
    channels = 1
    # The note file
    filename = 'tests/notefile.txt'
    # Play the song
    play_song(sampling_rate,bits,channels,filename)

if __name__=="__main__":
    main()
