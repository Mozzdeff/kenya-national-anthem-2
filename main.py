# Kenya National Anthem

from microbit import *
import music

# Define the notes and their durations
notes = [
    'C4:4', 'E4:4', 'G4:4', 'C5:4', 'E5:4', 'G5:4', 'C6:8',
    'G5:4', 'E5:4', 'C5:4', 'G4:4', 'E4:4', 'C4:8',
    'G4:4', 'B4:4', 'D5:4', 'G5:4', 'B5:4', 'D6:4', 'G6:8',
    'D6:4', 'B5:4', 'G5:4', 'D5:4', 'B4:4', 'G4:8',
    'D5:4', 'F#5:4', 'A5:4', 'D6:4', 'F#6:4', 'A6:4', 'D7:8'
]

# Play the notes
music.play(notes)

