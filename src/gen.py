#!/usr/bin/python3

import sys

from miparser import Note, Track, Segment, Song
from random import randint, seed, choice
from copy import deepcopy

from bass import add_bass
from bass_guitar import add_bass_guitar
from drums import add_drums
from sound_effects import add_sound_effects

out = "out.mid"
if len(sys.argv) > 1:
    out = sys.argv[1]

se = randint(0, 1000000)
print(se)
seed(se)

tpb = 64
bpm = randint(70,120)

s = Song(tpb, bpm)

s = add_bass_guitar(s, tpb=tpb)
s = add_bass(s, tpb=tpb)
s = add_drums(s, tpb=tpb)
s = add_sound_effects(s, tpb=tpb)

mid = s.toMidi()
mid.save(out)

