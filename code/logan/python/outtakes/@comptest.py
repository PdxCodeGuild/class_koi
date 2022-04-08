import mingus.core.progressions as progressions
import mingus.core.chords as chords

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

from mingus.midi import midi_file_out

solo_progression = [(chords.minor_triad("D"), 2), (chords.major_triad("Bb"), 2), (chords.major_triad("C"), 2), (chords.major_triad("A"), 2)]


composition = Composition()
lead_track = Track()
rhyth_track = Track()
bass_track = Track()

def simpbass(chord, bar, denominator):
    for _ in range(denominator):
        note = chord[0]
        note = Note(note)
        note.octave_down()
        bar.place_notes(note, denominator)

bass_bar = Bar()
bass_denom = 8
for tupe in solo_progression:
    b_chord = tupe[0]
    for _ in range(tupe[1]):
        bass_bar.empty()
        simpbass(b_chord, bass_bar, bass_denom)
        bass_track.add_bar(bass_bar)

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

midi_file_out.write_Track("tracks/basstest.mid", bass_track, 120, 0)