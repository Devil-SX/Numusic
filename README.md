# Numusic

Utilize mathematical operators to manipulate music!

Python>=10

# Play a chord

```
chord = HarmNote(scale=0) * 0.3 + HarmNote(scale=2) * 0.3 + HarmNote(scale=4) * 0.3
chord.play()
```

# Play a scale

```
note = HarmNote()
for i in range(8):
    note.play()
    note += 2
```