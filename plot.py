import pyaudio
import numpy as np

CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

print("* recording")

frames = np.array([])

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)

    a = np.frombuffer(data, dtype=np.int16)
    m = np.mean(a)
    print(f"Mean={m}")
    frames = np.concatenate([frames, a])


print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


import matplotlib.pyplot as plt


# sampling interval
ts = 1.0 / len(frames)
t = range(0, len(frames))

fig = plt.figure(figsize=(100, 4))
plt.figure(figsize=(100, 4))
plt.plot(t, frames, "r")
plt.ylabel("Amplitude")

plt.savefig("wave")
