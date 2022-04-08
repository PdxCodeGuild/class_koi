## Lots of imports from Mingus
## This looks tacky, but the module is kinda picky and it helps me to see them like this...

import mingus.core.progressions as progressions
import mingus.core.chords as chords

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar

from mingus.midi import midi_file_out

###################################################################################################

# ## I can modify these values to grab chords from progressions by their degree and quality.

# progression = ["I", "ii", "iii", "IV", "V", "vi", "dim"]
# progression_arpeggios = progressions.to_chords(progression, "C")

####################################################################################################
## Python Clips 0.1 Alpha

##### Arpeggio Maker
## Name the clip
bar1name = "arpeggiotest"
bar1 = Bar()
bar1_tonic = "C" # tonic note of the arpeggio
chord = chords.major_triad(bar1_tonic) #Major
# chord = chords.minor_triad(bar1_tonic) #Minor
# chord = chords.diminished_triad(bar1_tonic) #Diminished
# chord = ...

## Standard Slicing # May not really need slicing sections
start = 0
end = 3
step = 1

## Slicing Other
# start = 1 
# end = 0
# step = 1

## Reverse Slicing
# chord.reverse()
# chord.sort() # probably not worth implementing but funny :)

passes = 4
note_denom = 6
for _ in range(passes):
## Change chord selector mechanism?
    for note in chord[start:end:step]:
        # note = Note()
        bar1.place_notes(note, note_denom)

# ## Simple Bassline Maker will write here
# bar2 = Bar()
# ### Simple Tonic Bassline Maker
# for _ in range(8):
#     note = Note("A")
#     note.octave_down()
#     bar2.place_notes(note, 8)


# ### Harmony Maker will write here
# bar3 = Bar()
# ### Harmony Maker
# for _ in range(8):
#     chordgrab = chords.major_triad("C")
#     notes = NoteContainer()
#     notes.add_notes(chordgrab)
#     bar3.place_notes(notes, 8)

##3 Lead Line Maker
### Work in progress!!  Come back later
# for _ in range(8):
#     note = Note("A")
# #    # note.octave_down()
#     bar2.place_notes(note, 8)



################################


### Output
## Uncomment and adjust filename to run
# midi_file_out.write_Bar(f"{bar1name}.mid", bar1, 120, 1)
# midi_file_out.write_Bar("dpbasstest.mid", bar2, 120, 1)
# midi_file_out.write_Bar("harmonytest.mid", bar3, 120, 1)

# print(progression_arpeggios)

# print(chord)