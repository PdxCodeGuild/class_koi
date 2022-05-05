## Project Purple 0.1AA ##
#################################

### for acquiring and using music theoretical data
from typing import final
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
from functions import arp
from functions import arpreturn
from functions import gallopbass

### feed
## The chord progression to be automated over tupled with the number of bars the chord lingers.
solo_prog = [(chords.minor_triad("D"), 2), (chords.major_triad("Bb"), 2), (chords.major_triad("C"), 2), (chords.major_triad("A"), 2)]

### coming soon!  Do multiple progressions at once in the same song...a whole song at once!  Just loop a the list of progressions...
### progs = []

### composition
final_comp = Composition()
## adjustable composition Parameters
bpm = 120
loops = 0
 
### open MIDI tracks and name them
lead_track = Track()
lead_track.name = "steady arpeggios"
lead2_track = Track()
lead2_track.name = "steady returning arpeggios"

rhythm_track = Track()
rhythm_track.name = "steady simple harmony"

bass_track = Track()
bass_track.name = "steady simple bass"
bass2_track = Track()
bass2_track.name = "galloping bass"

blackmore_track = Track()
blackmore_track.name = "Blackmore"



### track writing -- these will be condensed to functions in future versions!!

## write the bass
bass_denom = 8 # Choose what length of note you want to take as a parameter
for tupe in solo_prog: # Cycle through the progression(s) to populated with notes...
    bass_chord = tupe[0]
    for _ in range(tupe[1]): # This repeats note population for correct # of bars.
        # bass_bar = gallopbass(bass_chord)
        bass_bar = simpbass(bass_chord, bass_denom)
        bass_track.add_bar(bass_bar)
## write the rhythm
rhythm_denom = 8 # Choose what length of note you want to take as a parameter
for tupe in solo_prog: # Cycle through the progression(s) to populated with notes...
    rhythm_chord = tupe[0]
    for _ in range(tupe[1]): # This repeats note population for correct # of bars.
        rhythm_bar = simprhythm(rhythm_chord, rhythm_denom)
        rhythm_track.add_bar(rhythm_bar)
## write the lead - more interesting versions coming soon!  going to be a lot harder now that I know the scales submodule is not fully functional...
lead_denom = 16
for tupe in solo_prog: # Cycle through the progression(s) to populated with notes...
    lead_chord = tupe[0] # This repeats note population for correct # of bars.
    for _ in range(tupe[1]):
        lead_bar = arp(lead_chord, lead_denom)
        lead_track.add_bar(lead_bar)
## write beats -- need to work through the note-mapping into sample like Ableton's, goofs up when octave is off and correct values are presently unknown.
## COMING SOON ##


### write Blackmore (hard code)
## I could make these generalizable and not hard-coded if mingus.scales was finished...
## ...I could add the functionality without modifying the package itself, but it will take time.
## note define
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
## bar 1
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

## bar 2
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

## bar 3
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

## bar 4
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
## bar 5
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

### write alternate lead
lead2_denom = 16
for tupe in solo_prog: # Cycle through the progression(s) to populated with notes...
    lead2_chord = tupe[0] # This repeats note population for correct # of bars.
    for _ in range(tupe[1]):
        lead2_bar = arpreturn(lead2_chord, lead2_denom)
        lead2_track.add_bar(lead2_bar)

### write galloping bass
bass2_denom = 8 # Choose what length of note you want to take as a parameter
for tupe in solo_prog: # Cycle through the progression(s) to populated with notes...
    bass2_chord = tupe[0]
    for _ in range(tupe[1]): # This repeats note population for correct # of bars.
        # bass_bar = gallopbass(bass_chord)
        bass2_bar = gallopbass(bass2_chord)
        bass2_track.add_bar(bass2_bar)


### Output
## Gather the tracks for output
final_comp.add_track(bass_track)
final_comp.add_track(rhythm_track)
final_comp.add_track(blackmore_track)
final_comp.add_track(lead_track)
final_comp.add_track(bass2_track)
final_comp.add_track(lead2_track)

## Output tracks
# midi_file_out.write_Track("tracks/basstest.mid", bass_track, 120, 0)
midi_file_out.write_Composition("compositions/projectpurple.mid", final_comp, bpm, loops)


## Print *something* so non-Logan users aren't like "wtf just happened?"
print("""
Your MIDI awaits in /compositions.
""")

