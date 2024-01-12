"""PyAudio Example: Play a wave file (callback version)."""

import wave
import time
import sys

import pyaudio

p = pyaudio.PyAudio()

CHANNELS = 1
RATE = 44100
CHUNK = 2048
FORMAT = pyaudio.paInt16


def callback(in_data, frame_count, time_info, status):
    print(f"Called count={frame_count}")
    # return (in_data, pyaudio.paComplete)
    return (in_data, pyaudio.paContinue)


stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    stream_callback=callback,
)


DURATION = 1  # seconds
start = time.time()
while stream.is_active() and (time.time() - start) < DURATION:
    time.sleep(0.1)

stream.close()
p.terminate()
