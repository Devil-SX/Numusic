from Numusic import HarmNote, SingleNote


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


c4 = HarmNote(scale=-9)
c4.play()

play_major_key(c4)
play_major_key(c4 + 12)