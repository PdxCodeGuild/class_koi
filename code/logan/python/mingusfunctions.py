import mingus.core.progressions as progressions
import mingus.core.chords as chords

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.midi import midi_file_out


#################
## Work in Progress ##
## Functions ##

## Harmony Maker for triads
## Work in progress!!
## Notes: I'm not sure the repl is worth it, actually!
def harmony():
    length = 1
    bar = Bar()
    chord = NoteContainer()
    tonic = input("What is the tonic...?")
    # bpm = input("What BPM?...") # we'll default to 120bpm for now
    quality = input("What is the quality?...")
    if quality == "m":
        triad = chords.minor_triad(tonic)
    if quality == "M":
        triad = chords.major_triad(tonic)
    chord.add_notes(triad)
    repl = "3"
    while repl != "0":
        repl = input("1 for a note, 2 for a rest, 0 to quit...")
        if repl == ("1" or "2"):
            length: input("How long?...")
            if repl == "1":
                bar.place_notes(triad, int(length))
            if repl == "2":
                bar.place_rest(int(length))
    loops = input("How many loops?...")
    filename = input("Filename??... (no extension)")
    midi_file_out.write_Bar(f"{filename}.mid", bar, 120, int(loops))
    return

harmony()


##################################
#  Works in progress
## Arpeggio Maker



