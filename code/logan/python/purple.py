## All right, hold tight, I'm a Highway Staaaaaaaaaaar!! ##

## Let's learn Mingus ##
import mingus.core.progressions as progressions
import mingus.core.chords as chords

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.midi import midi_file_out

## Fun with chord substitutions

# progression = ["I", "iii", "V", "I"]
# # test = progressions.to_chords(progression, "C")
# # for chord in test:
# #     print(chords.determine(chord))

# print(progressions.substitute(progression, 0))

q1 = Bar()

a = Note("A", 4)
bb = Note("Bb", 4)
c = Note("C", 5)
d = Note("D", 5)
e = Note("E", 5)
elow = Note("E", 4)
ahigh = Note("A", 5)
ab = Note("Ab", 5)
g = Note("G", 5)
gb = Note("Gb", 5)
f = Note("F", 5)
eb = Note("Eb", 5)
db = Note("Db", 5)

# lick1 = NoteContainer()
# lick1.add_notes([a, bb, c, c])

# Blackmore Lick 1
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

# Blackmore Lick 2
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

# Blackmore Lick 3
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
#########################
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


# midi_file_out.write_Bar("BlackmoreLick4.mid", q4, 120, 1)
# midi_file_out.write_NoteContainer("test.mid", lick1)

midi_file_out.write_Bar("BlackmoreTest.mid", q1, 120, 1)





##########################

# import mingus.core.notes as notes
# print(notes.is_valid_note("C")) ## works

# import mingus.core.chords as chords
# print(chords.determine("E", "G#", "D", "G")) # Doesn't work!  It says "E", but that's the Hendrix chord -- a dom 7 with an augmented 9.

# import mingus
# print(mingus.core.notes.is_valid("C")) # Doesn't work

## Qs...
# notes.to_minor("A")  Why doesn't this work?