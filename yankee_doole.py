from Numusic import HarmNote

c4 = HarmNote(scale=-9)
d4 = c4 + 2
e4 = c4 + 4
f4 = c4 + 5
g3 = c4 - 5
a3 = c4 - 3
b3 = c4 - 1

song = [c4, c4, d4, e4,
        d4, e4, d4, g3,
        c4, c4, d4, e4,
        c4, c4, b3, g3,
        c4, c4, d4, e4,
        f4, e4, d4, c4,
        b3, g3, a3, b3,
        c4, c4, c4, c4]

for note in song:
    note.play()