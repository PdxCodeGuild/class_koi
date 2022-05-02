# This is stuff I found online that I'm testing

from mido import MidiFile
from mido import MidiTrack
from mido import Message

testmid1 = MidiFile("BlackmoreLick1.mid", clip=True)
testmid2 = MidiFile("BlackmoreLick2.mid", clip=True)
newmidi = MidiFile()
# newtrack = MidiTrack()
# newmidi.tracks.append(newtrack)
# newmidi.tracks.append(track)

# for message in testmid1.tracks:
#     track = MidiTrack()
#     newmidi.tracks.append(track)
# for track in testmid2.tracks:
#     track = MidiTrack()
#     newmidi.tracks.append(track)
# for i, track in enumerate(testmid1.tracks):
#     newtrack.append(track)
# for i, track in enumerate(testmid2.tracks):
#     newtrack.append(track)

newmidi.tracks.append(testmid1.tracks)
newmidi.tracks.append(testmid2.tracks)
    

newmidi.save("BlackmoreSplice.mid")








###########################################################
# import midi

# pattern1 = midi.__loader__
# ("BlackmoreLick1.mid")
# pattern2 = midi.read_midifile("BlackmoreLick2.mid")

# pattern = midi.Pattern()

# for track in pattern1:
#     pattern.append(track)

# for track in pattern2:
#     pattern.append(track)

# midi.write_midifile('BlackmoreJoin.mid', pattern)

## Also doesn't work!

########################################################
# import pygame
# pygame.init()

# pygame.mixer.music.load("BlackmoreLick1.mid")
# pygame.mixer.music.play()\

## The internet lied to me, it doesn't work!