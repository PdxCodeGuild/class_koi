import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
# import mingus.core.keys as keys
import mingus.core.notes as notes

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

from mingus.midi import midi_file_out
from numpy import roots


# print((chords.minor_triad("D")[0]))

# rel_major = scales.get_notes("F")
solo_progression = [(chords.minor_triad("D"), 2), (chords.major_triad("Bb"), 2), (chords.major_triad("C"), 2), (chords.major_triad("A"), 2)]
chord_select = solo_progression[0]
# scale_1 = scales.Major("F")
# print(scale_1)

# print(rel_major)

# phyrigian_tonic = rel_major[2]
# print(scales.Phrygian(phyrigian_tonic))

## bar length licks

## Phyrigian Lick
# root = "D"
# root_as_num = notes.note_to_int(root)
# print(root_as_num)
# firstnote = root_as_num + 7
# secondnote = root_as_num + 1
# thirdnote = secondnote + 2

def bmphyrigian1(chord):
    bar = Bar()

    root = chord[0][0]
    root_as_num = notes.note_to_int(root)
    firstnote = root_as_num + 7
    secondnote = firstnote + 1
    thirdnote = secondnote + 2
    firstnote = Note()
    secondnote = Note()
    thirdnote = Note()
    bar.place_notes(firstnote, 16)
    bar.place_notes(secondnote, 16)
    bar.place_notes(thirdnote, 16)
    bar.place_notes(thirdnote, 16)
    return bar

clip = bmphyrigian1(chord_select)

midi_file_out.write_Bar("clips/BlackmoreTest.mid", clip, 120, 1)

# ##############
# def simpbass(chord, denominator):
    
#     bar = Bar()
#     note = chord[0]
#     note = Note(note)
#     note.octave_down()
#     for _ in range(denominator):
#         bar.place_notes(note, denominator)
#     return bar
    







########################################




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