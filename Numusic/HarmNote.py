from .Note import SingleNote
import numpy as np


class HarmNote(SingleNote):
    def __init__(self, duration=0.5, sample_rate = 44100, scale=0) -> None:
        super().__init__(duration, sample_rate, scale)


    def _gen_wave(self):
        t = np.linspace(
            0, self.duration, int(self.sample_rate * self.duration), endpoint=False
        )
        self.wave = 0.5 * np.sin(2 * np.pi * self.frequency * t)
        self.wave += 0.5**2 * np.sin(2 * np.pi * 2 * self.frequency * t)
        self.wave += 0.5**3 * np.sin(2 * np.pi * 3 * self.frequency * t)
        self.wave = np.exp(-3 * t / self.duration) * self.wave # decay


if __name__ == "__main__":
    note = HarmNote()
    note.play()
    # note.plot()
    
    chord = HarmNote(scale=0) * 0.3 + HarmNote(scale=2) * 0.3 + HarmNote(scale=4) * 0.3
    chord.play()

    for i in range(8):
        note = note + 1
        note.play()

    for i in range(8):
        note = note - 1
        note.play()