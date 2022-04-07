import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

from mingus.midi import midi_file_out


# print((chords.minor_triad("D")[0]))

rel_major = scales.Diatonic("F")
solo_progression = [(chords.minor_triad("D"), 2), (chords.major_triad("Bb"), 2), (chords.major_triad("C"), 2), (chords.major_triad("A"), 2)]

# scale_1 = scales.Major("F")
# print(scale_1)

print(rel_major)

# phyrigian_tonic = rel_major[2]
# print(scales.Phrygian(phyrigian_tonic))

## bar length licks

## Phyrigian Lick




# # print(solo_progression[0][0])

# for tupe in solo_progression:
#     chord = tupe[0]
#     print(chord)


# # test = ["E", "G", "B"]

# # # print(test[0:3:1])
# # print(test[1:0:1])

# # ## Can I make it look like ["G", "B", "E"]?

# tupe = (1,2)

# print(tupe[1])