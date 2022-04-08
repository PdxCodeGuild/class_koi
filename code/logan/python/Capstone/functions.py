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

## These can and will be improved.

def simpbass(chord, denominator):
    "Writes really simple basslines"
    bar = Bar()
    note = chord[0]
    note = Note(note)
    note.octave_down()
    for _ in range(denominator):
        bar.place_notes(note, denominator)
    return bar

def gallopbass(chord):
    "Writes galloping bass a la Iron Maiden"
    bar = Bar()
    note = chord[0]
    note = Note(note)    
    note.octave_down()
    for _ in range(4):
        bar.place_notes(note, 8)
        bar.place_notes(note, 16)
        bar.place_notes(note, 16)
    return bar

def simprhythm(chord, denominator):
    "Writes really simple harmony like a rhythm guitar or piano"
    bar = Bar()
    notes = NoteContainer()
    notes.add_notes(chord)
    for _ in range(denominator):
        bar.place_notes(notes, denominator)
    return bar

def arp(chord, denominator):
    "Writes simple steady ascending arpeggios"
    bar = Bar()
    for note in chord:
        note = Note()
    for _ in range(10):
        for note in chord:
            bar.place_notes(note, denominator)
    return bar

def arpreturn(chord, denominator):
    "Writes steady up and down arpeggios, like a sweep-picking guitarist"
    bar = Bar()
    for note in chord:
        note = Note()
    chord_r = []
    for note in chord:
        chord_r.append(note)
    chord_r.reverse()
    for _ in range(10):
        for note in chord:
            bar.place_notes(note, denominator)
        for note in chord_r:
            bar.place_notes(note, denominator)
    return bar

def drums1():
    """
    Nothing special -- my first beat!  Set instrument to Late Nite Drum Kit in Ableton
    UNDER CONSTRUCTION!  Need to find a way to pair notes to certain drums,
    either for a specific Ableton set or somehow coded in the MIDI.
    """
    bar = Bar()
    # bass_d = "C"
    # splat = "G"
    bass_d = Note("C", 2) # This works!
    splat = Note("F", 2)  # This doesn't get the right note for snare and I don't know why.
    # bass_d.octave_down()
    # bass_d.octave_down()
    # splat.octave_down()
    # splat.octave_down()
    bar.place_notes(bass_d, 2)
    bar.place_notes(splat, 2)
    return bar

# test = drums1()

# midi_file_out.write_Bar("compositions/beattest.mid", test, 120, 1)