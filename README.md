# Numusic

![Static Badge](https://img.shields.io/badge/python-%3E%3D3.10-blue?logo=python&labelColor=%23F7DF1E)



Utilize mathematical operators to manipulate music!


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