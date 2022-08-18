from pydub import AudioSegment
import random as rn

sandman = AudioSegment.from_mp3("sandman.mp3")
marimba = AudioSegment.from_mp3("bright_marimba.mp3")
string = AudioSegment.from_mp3("jarble_tweeze_string.mp3")
bell = AudioSegment.from_mp3("outland_bell.mp3")
choir = AudioSegment.from_mp3("spacious_choir.mp3")

for _ in range(10):
    cis_sa = rn.randint(0, 4)
    cis_ma = rn.randint(0, 4)
    cis_st = rn.randint(0, 4)
    cis_be = rn.randint(0, 4)

    if cis_sa
    


# mix sound2 with sound1, starting at 5000ms into sound1)
output = sound1.overlay(sound2, position=5000)

# save the result
output.export("mixed_sounds.mp3", format="mp3")
