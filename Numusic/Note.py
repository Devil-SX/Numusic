from __future__ import annotations

import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from matplotlib import pyplot as plt
import copy

A4_FREQ = 440


def get_freq(scale: int):
    return A4_FREQ * 2 ** (scale / 12)


class Note:
    def __init__(self, duration=0.5, sample_rate=44100):
        self.duration = duration
        self.sample_rate = sample_rate
        self.wave = None

    def play(self):
        wave = np.int16(self.wave * 32767)
        audio = AudioSegment(
            wave.tobytes(),
            frame_rate=self.sample_rate,
            sample_width=wave.dtype.itemsize,
            channels=1,
        )
        play(audio)

    def plot(self):
        plt.plot(self.wave[0 : int(self.sample_rate * self.duration / 50)])
        plt.show()

    def __mul__(self, scale) -> Note:
        temp = copy.deepcopy(self)
        temp.wave = temp.wave * scale
        return temp

    def __add__(self, note: Note) -> Note:
        temp = copy.deepcopy(self)
        temp.wave = temp.wave + note.wave
        return temp

    def __sub__(self, note: Note) -> Note:
        temp = copy.deepcopy(self)
        temp.wave = temp.wave - note.wave
        return temp


class SingleNote(Note):
    def __init__(self, duration=0.5, sample_rate=44100, scale=0) -> None:
        super().__init__(duration, sample_rate)
        self.scale = scale
        self.frequency = get_freq(self.scale)
        self._gen_wave()

    def __add__(self, arg: int | Note) -> SingleNote | Note:
        match arg:
            case int(half_step):
                temp = copy.deepcopy(self)
                temp.scale += half_step
                temp.frequency = get_freq(temp.scale)
                temp._gen_wave()
                return temp
            case Note():
                return super().__add__(arg)

    def __sub__(self, arg: int | Note) -> SingleNote | Note:
        match arg:
            case int(half_step):
                temp = copy.deepcopy(self)
                temp.scale -= half_step
                temp.frequency = get_freq(temp.scale)
                temp._gen_wave()
                return temp
            case Note():
                return super().__sub__(arg)

    def _gen_wave(self):
        t = np.linspace(
            0, self.duration, int(self.sample_rate * self.duration), endpoint=False
        )
        self.wave = 0.5 * np.sin(2 * np.pi * self.frequency * t)


if __name__ == "__main__":
    note = SingleNote()
    note.play()

    chord = SingleNote(scale=0) * 0.3 + SingleNote(scale=2) * 0.3 + SingleNote(scale=4) * 0.3
    chord.play()

    for i in range(8):
        note = note + 1
        note.play()

    for i in range(8):
        note = note - 1
        note.play()
