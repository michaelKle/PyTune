import pyaudio
import numpy as np
import numpy.fft

# G= 196 Hz
# D= 293.7 Hz
# A= 440Hz
# E= 659.3 Hz

CHUNK = 8096
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 30

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
    # print(f"Mean={m}")
    frames = np.concatenate([frames, a])

    X = np.fft.fft(a)
    freq = np.fft.fftfreq(len(a)) * RATE
    Xabs = np.abs(X)
    cutoff = np.argmax(freq > 700.0)
    Xabs = Xabs[:cutoff]
    freq = freq[:cutoff]
    i = Xabs.argmax()

    #    print(f"Freq={freq[i]}")
    print(f"Freq={abs(freq[i])}")


print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


sampleOffset = int(len(frames) / 2)
frames = frames[sampleOffset : sampleOffset + CHUNK]

# import matplotlib.pyplot as plt


# X = np.fft.fft(frames)
# freq = np.fft.fftfreq(len(frames))
# freq = freq * RATE

# i = np.argmax(freq > 800.0)

# X = X[:i]
# freq = freq[:i]
# Xabs = np.abs(X)

# plt.figure(figsize=(12, 6))

# plt.stem(freq, Xabs, "b", markerfmt=" ", basefmt="-b")
# plt.xlabel("Freq (Hz)")
# plt.ylabel("FFT Amplitude |X(freq)|")
# plt.xlim(0, 800)
# plt.savefig("ffp")
