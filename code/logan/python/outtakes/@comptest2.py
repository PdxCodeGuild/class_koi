import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

from mingus.midi import midi_file_out

solo_progression = [(chords.minor_triad("D"), 2), (chords.major_triad("Bb"), 2), (chords.major_triad("C"), 2), (chords.major_triad("A"), 2)]

### Composition
c = Composition()
## Composition Parameters
bpm = 120
loops = 0


### Tracks
lead_track = Track()
rhythm_track = Track()
bass_track = Track()

## Functions

def simpbass(chord, denominator):
    bar = Bar()
    note = chord[0]
    note = Note(note)
    note.octave_down()
    for _ in range(denominator):
        bar.place_notes(note, denominator)
    return bar

def simprhythm(chord, denominator):
    bar = Bar()
    notes = NoteContainer()
    notes.add_notes(chord)
    for _ in range(denominator):
        bar.place_notes(notes, denominator)
    return bar


### Write the bass
bass_denom = 8
for tupe in solo_progression:
    bass_chord = tupe[0]
    for _ in range(tupe[1]):
        bass_bar = simpbass(bass_chord, bass_denom)
        bass_track.add_bar(bass_bar)

### Write the rhythm
rhythm_denom = 8
for tupe in solo_progression:
    rhythm_chord = tupe[0]
    for _ in range(tupe[1]):
        rhythm_bar = simprhythm(rhythm_chord, rhythm_denom)
        rhythm_track.add_bar(rhythm_bar)


# # Simple Bassline Maker
# for _ in range(8):
#     note = Note("A")
#     note.octave_down()
#     !!!.place_notes(note, 8)

# ### Harmony Maker
# for _ in range(8):
#     chordgrab = chords.major_triad("C")
#     notes = NoteContainer()
#     notes.add_notes(chordgrab)
#     bar3.place_notes(notes, 8)

c.add_track(rhythm_track)
c.add_track(bass_track)

# midi_file_out.write_Track("tracks/basstest.mid", bass_track, 120, 0)
midi_file_out.write_Composition("compositions/compositiontest.mid", c, bpm, loops)