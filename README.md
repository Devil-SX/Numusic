# Numusic

![Static Badge](https://img.shields.io/badge/python-%3E%3D3.10-blue?logo=python&labelColor=%23F7DF1E)



Utilize mathematical operators to manipulate music!


# Play a chord

```python
chord = HarmNote(scale=0) * 0.3 + HarmNote(scale=2) * 0.3 + HarmNote(scale=4) * 0.3
chord.play()
```

# Play a scale

```python
note = HarmNote()
for i in range(8):
    note.play()
    note += 2 # 2 halp step
```

# Play C Major


```python
def play_major_key(tonic: SingleNote):
    tonic.play()
    for i in range(2):
        tonic += 2
        tonic.play()

    tonic += 1
    tonic.play()

    for i in range(3):
        tonic += 2
        tonic.play()

play_major_key(c4)
play_major_key(c4 + 12)
```

# Play Yankee Doodle

```python
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
```