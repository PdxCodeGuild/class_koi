## Project Purple 0.1AA ##
#################################

### for acquiring and using music theoretical data
import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

### for writing notes, chords bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

### for writing MIDIS 
from mingus.midi import midi_file_out

### for "improvisation" along certain parameters -- for future versions
## import random

### my functions
## these compose things for me algorithmically
from functions import simpbass
from functions import simprhythm
from functions import arplead

### feed
## The chord progression to be automated over tupled with the number of bars the chord lingers.
solo_prog = [(chords.minor_triad("D"), 2), (chords.major_triad("Bb"), 2), (chords.major_triad("C"), 2), (chords.major_triad("A"), 2)]

### coming soon!  Do multiple progressions at once in the same song...
### progs = []

### composition
final_comp = Composition()
## composition Parameters
bpm = 120
loops = 0


### tracks
lead_track = Track()
lead_track.name = "regular steady lead"
rhythm_track = Track()
rhythm_track.name = "regular steady rhythm "
bass_track = Track()
bass_track.name = "regular steady bass"
blackmore_track = Track()
blackmore_track.name = "Blackmore"


### track writing -- these will be condenses to functions in future versions
## write the bass
bass_denom = 8
for tupe in solo_prog:
    bass_chord = tupe[0]
    for _ in range(tupe[1]):
        bass_bar = simpbass(bass_chord, bass_denom)
        bass_track.add_bar(bass_bar)
## write the rhythm
rhythm_denom = 8
for tupe in solo_prog:
    rhythm_chord = tupe[0]
    for _ in range(1):
        rhythm_bar = simprhythm(rhythm_chord, rhythm_denom)
        rhythm_track.add_bar(rhythm_bar)
## write the lead - more interesting versions coming soon!  going to be a lot harder now that I know the scales submodule is not fully functional...
# lead_denom = 8
# for tupe in solo_prog:
#     rhythm_chord = tupe[0]
#     for _ in range(tupe[1]):
#         rhythm_bar = simprhythm(rhythm_chord, rhythm_denom)
#         rhythm_track.add_bar(rhythm_bar)


### write Blackmore (hard code)
## Notes
elow = Note("E", 4)
a = Note("A", 4)
bb = Note("Bb", 4)
c = Note("C", 5)
d = Note("D", 5)
e = Note("E", 5)
elow = Note("E", 4)
ab = Note("Ab", 5)
g = Note("G", 5)
gb = Note("Gb", 5)
f = Note("F", 5)
eb = Note("Eb", 5)
db = Note("Db", 5)
ahigh = Note("A", 5)
## Bar 1
q1 = Bar()
q1.place_notes(a,16)
q1.place_notes(bb,16)
q1.place_notes(c,16)
q1.place_notes(c,16)
q1.place_notes(a,16)
q1.place_notes(bb,16)
q1.place_notes(c,16)
q1.place_notes(c,16)
q1.place_notes(a,16)
q1.place_notes(bb,16)
q1.place_notes(c,16)
q1.place_notes(c,16)
q1.place_notes(a,16)
q1.place_notes(bb,16)
q1.place_notes(c,16)
q1.place_notes(c,16)

blackmore_track.add_bar(q1)
blackmore_track.add_bar(q1)
## Bar 2
q2 = Bar()
q2.place_notes(bb, 16)
q2.place_notes(c, 16)
q2.place_notes(d, 16)
q2.place_notes(d, 16)
q2.place_notes(bb, 16)
q2.place_notes(c, 16)
q2.place_notes(d, 16)
q2.place_notes(d, 16)
q2.place_notes(bb, 16)
q2.place_notes(c, 16)
q2.place_notes(d, 16)
q2.place_notes(d, 16)
q2.place_notes(bb, 16)
q2.place_notes(c, 16)
q2.place_notes(d, 16)
q2.place_notes(d, 16)

blackmore_track.add_bar(q2)
blackmore_track.add_bar(q2)
## Bar 3
q3 = Bar()
q3.place_notes(c, 16)
q3.place_notes(d, 16)
q3.place_notes(e, 16)
q3.place_notes(e, 16)
q3.place_notes(c, 16)
q3.place_notes(d, 16)
q3.place_notes(e, 16)
q3.place_notes(e, 16)
q3.place_notes(c, 16)
q3.place_notes(d, 16)
q3.place_notes(e, 16)
q3.place_notes(e, 16)
q3.place_notes(c, 16)
q3.place_notes(d, 16)
q3.place_notes(e, 16)
q3.place_notes(e, 16)

blackmore_track.add_bar(q3)
blackmore_track.add_bar(q3)
## Bar 4
q4 = Bar()
q4.place_notes(ahigh,16)
q4.place_notes(ab,16)
q4.place_notes(elow,16)
q4.place_notes(elow,16)
#
q4.place_notes(ab,16)
q4.place_notes(g,16)
q4.place_notes(elow,16)
q4.place_notes(elow,16)
#
q4.place_notes(g,16)
q4.place_notes(gb,16)
q4.place_notes(elow,16)
q4.place_notes(elow,16)
#
q4.place_notes(gb,16)
q4.place_notes(f,16)
q4.place_notes(elow,16)
q4.place_notes(elow,16)

blackmore_track.add_bar(q4)
## Bar 5
q5 = Bar()
q5.place_notes(f,16)
q5.place_notes(e,16)
q5.place_notes(elow,16)
q5.place_notes(elow,16)
#
q5.place_notes(e,16)
q5.place_notes(eb,16)
q5.place_notes(elow,16)
q5.place_notes(elow,16)
#
q5.place_notes(eb,16)
q5.place_notes(d,16)
q5.place_notes(elow,16)
q5.place_notes(elow,16)
#
q5.place_notes(d,16)
q5.place_notes(db,16)
q5.place_notes(elow,16)
q5.place_notes(elow,16)

blackmore_track.add_bar(q5)

##############################

### Output
## Gather the tracks for output
final_comp.add_track(bass_track)
final_comp.add_track(rhythm_track)
final_comp.add_track(blackmore_track)
#final_comp.

## Output tracks
# midi_file_out.write_Track("tracks/basstest.mid", bass_track, 120, 0)
midi_file_out.write_Composition("compositions/copytest.mid", final_comp, bpm, loops)