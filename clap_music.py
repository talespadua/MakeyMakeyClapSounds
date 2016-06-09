#!/usr/bin/env/python

import pygame
import numpy as np
import sys
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
    if volume<0.0: volume = 0.0
    if volume>1.0: volume = 1.0
    max_value = int_max_value(bits)
    note = []
    for x in range(0, int(sampling_rate*duration)):
        value = volume * max_value * np.sin(2 * np.pi * freq * x / sampling_rate)
        note.append(value)
    return note

def create_melody(bits, sampling_rate, volumes, freqs, durations):
    melody = []
    note = create_note(bits, sampling_rate, volumes, freqs, durations)
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
    note_name = note[0].upper()
    note_octave = int(note[1])
    notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    baseind = 9
    noteind = notes.index(note_name)
    n = noteind - baseind
    n += (4-note_octave)*12
    a = 1.059463094359
    f0 = 440
    freq = f0 * pow(a, n)
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
    pygame.mixer.pre_init(sampling_rate, -bits, channels, 512)
    # pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()

    pygame.init()
    # screen size
    screen_width = 300
    screen_height = 300
    running = True
    clock = pygame.time.Clock()
    blocks = []
    game_display = pygame.display.set_mode((screen_width, screen_height))
    with open(filename, 'r') as f:
        for line in f:
            blocks.append(line)
    #blocks = contents.split()
    i = 0
    while(running):
        note, wait_duration, volume = blocks[i].split(':')
        # Note frequencies
        freqs = calculate_note_freq(note)
        wait_duration = float(wait_duration)
        melody = create_melody(bits, sampling_rate, volume, freqs, wait_duration)
        melody = np.array(melody).astype(np.int16)
        # Create the sound
        sound = make_sound(melody)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Play and loop
                    sound.play(0, int(wait_duration*1000))
                    # Stop after <duration>
                    pygame.time.delay(int(wait_duration*1000))
                    # # Stop playing
                    sound.stop()
                    if i < len(blocks) - 1:
                        i += 1
                    else:
                        pygame.time.delay(int(wait_duration*1000))
                        pygame.quit()
                        quit()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        clock.tick(10)



def main():
    # Set some variables
    sampling_rate = 8000
    bits = 16
    # In this case: mono
    channels = 1
    # The note file
    song = str(sys.argv[1])
    filename = "musics/" + song + ".txt"
    # Play the song
    play_song(sampling_rate, bits, channels, filename)

if __name__=="__main__":
    main()
