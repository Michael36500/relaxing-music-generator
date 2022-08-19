from pydub import AudioSegment
import random as rn
from tqdm import tqdm

bass = AudioSegment.from_wav("bass.wav")
DRdetonate = AudioSegment.from_wav("DRdetonate.wav")
DRmaster = AudioSegment.from_wav("DRmaster.wav")
hihat = AudioSegment.from_wav("hihat.wav")
keys = AudioSegment.from_wav("keys.wav")
pad = AudioSegment.from_wav("pad.wav")
piano = AudioSegment.from_wav("piano.wav")
print("empty")
output = AudioSegment.from_wav("empty.wav")

length_one_clip = 23000
length_total = 2 * 60 * 1000

loops = length_total // length_one_clip + 1

for lp in tqdm(range(loops)):
    bass = rn.randint(0,1)
    keys = rn.randint(0,1)
    pad = rn.randint(0,1)
    piano = rn.randint(0,1)

    drums = rn.randint(0,2)

    if bass == 1:
        output = output.overlay(bass, position=lp*length_one_clip)
    if keys == 1:
        output = output.overlay(keys, position=lp*length_one_clip)
    if pad == 1:
        output = output.overlay(pad, position=lp*length_one_clip)
    if piano == 1:
        output = output.overlay(piano, position=lp*length_one_clip)

    if drums == 0:
        output = output.overlay(DRdetonate, position=lp*length_one_clip)
    if drums == 1:
        output = output.overlay(DRmaster, position=lp*length_one_clip)
    if drums == 2:
        output = output.overlay(hihat, position=lp*length_one_clip)
        



# save the result
output.export("mixed_sounds.mp3", format="mp3")
