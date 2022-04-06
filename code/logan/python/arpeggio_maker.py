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

def triad_rock_forward(triad):
    new_triad = []
    new_triad.append(triad[1])
    new_triad.append(triad[2])
    new_triad.append(triad[0])
    return new_triad



##### Arpeggio Maker Sliced
## Name the clip
bar1name = "arpeggiotest"
bar1 = Bar()
bar1_tonic = "C" # tonic note of the arpeggio
chord = chords.major_triad(bar1_tonic) #Major
# chord = chords.minor_triad(bar1_tonic) #Minor
# chord = chords.diminished_triad(bar1_tonic) #Diminished
# chord = ...
triad_rock_forward(chord)


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



midi_file_out.write_Bar(f"{bar1name}.mid", bar1, 120, 1)