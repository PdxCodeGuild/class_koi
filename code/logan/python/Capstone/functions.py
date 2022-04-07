### For acquiring and using music theoretical data
import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

### For writing notes, chords bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

# import random
## Coming not soon, but usable in "freestyle" improvisation function

### For writing MIDIS 
from mingus.midi import midi_file_out

def simpbass(chord, denominator):
    "Writes really simple basslines"
    bar = Bar()
    note = chord[0]
    note = Note(note)
    note.octave_down()
    for _ in range(denominator):
        bar.place_notes(note, denominator)
    return bar

def simprhythm(chord, denominator):
    "Writes really simple harmony like a rhythm guitar or piano"
    bar = Bar()
    notes = NoteContainer()
    notes.add_notes(chord)
    for _ in range(denominator):
        bar.place_notes(notes, denominator)
    return bar

def arplead(chord, denominator):
    "Coming soon, but soon enough?? ;)"
    bar = Bar()
    for note in chord:
        note = Note()
    for _ in range(10):
        for note in chord:
            bar.place_notes(note, denominator)
    return bar