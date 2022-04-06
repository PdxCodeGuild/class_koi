import mingus.core.progressions as progressions
import mingus.core.chords as chords

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.midi import midi_file_out

# progression = ["vi", "V", "IV", "V"]
# progression_arpeggios = progressions.to_chords(progression, "C")

bar1 = Bar()


### Arpeggio Maker
# for _ in range(2):
#     for note in progression_arpeggios[3]:
#         # note = Note()
#         bar1.place_notes(note, 6)

bar2 = Bar()

### Simple Bassline Maker
# for _ in range(8):
#     note = Note("A")
#     note.octave_down()
#     bar2.place_notes(note, 8)

bar3 = Bar()

# ### Harmony Maker
# for _ in range(8):
#     chordgrab = chords.major_triad("C")
#     notes = NoteContainer()
#     notes.add_notes(chordgrab)
#     bar3.place_notes(notes, 8)



### Output
# midi_file_out.write_Bar("arpeggio4.mid", bar1, 120, 1)
# midi_file_out.write_Bar("dpbass3.mid", bar2, 120, 1)
# midi_file_out.write_Bar("harmony2.mid", bar3, 120, 1)

# print(progression_arpeggios)