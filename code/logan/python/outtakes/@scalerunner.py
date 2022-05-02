import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

from mingus.midi import midi_file_out

# Scales core is unfinished :( :( :( :( :( :(



solo_progression = [(chords.minor_triad("D"), 2), (chords.major_triad("Bb"), 2), (chords.major_triad("C"), 2), (chords.major_triad("A"), 2)]



# scale = scales.Phrygian("A")


composition = Composition()
lead_track = Track()
rhyth_track = Track()
bass_track = Track()

## Walkup Lick



######################################

# def simpbass(chord, denominator):
#     bar = Bar()
#     note = chord[0]
#     note = Note(note)
#     note.octave_down()
#     for _ in range(denominator):
#         bar.place_notes(note, denominator)
#     return(bar)

# # bass_bar = Bar()
# bass_denom = 8
# for tupe in solo_progression:
#     bass_chord = tupe[0]
#     for _ in range(tupe[1]):
#         bass_bar = simpbass(bass_chord, bass_denom)
#         bass_track.add_bar(bass_bar)
