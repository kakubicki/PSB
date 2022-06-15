def drawSubPlotSignalFromFile(filename):
    spf = wave.open(f"recordings/{filename}.wav", "r")
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "Int16")
    fs = spf.getframerate()

    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)

    Time = np.linspace(0, len(signal) / fs, num=len(signal))

    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(Time, signal)
    plt.show()

def drawSubSpectrogramFromFile(axis, x, y, filename):
    sample_rate, samples = wavfile.read(f"recordings/{filename}.wav")
    
    axis[x, y].specgram(samples, Fs=sample_rate)
    axis[x, y].set_title(filename)
    axis[x, y].set_ylabel('Frequency [Hz]')
    axis[x, y].set_xlabel('Time [sec]')

def drawSpectrograms():
    figure, axis = plt.subplots(3, 2)
    drawSubSpectrogramFromFile(axis, 0, 0, "Samogloska-A")
    drawSubSpectrogramFromFile(axis, 0, 1, "Samogloska-E")
    drawSubSpectrogramFromFile(axis, 1, 0, "Samogloska-I")
    drawSubSpectrogramFromFile(axis, 1, 1, "Samogloska-O")
    drawSubSpectrogramFromFile(axis, 2, 0, "Samogloska-U")
    drawSubSpectrogramFromFile(axis, 2, 1, "Samogloska-Y")
    plt.show()