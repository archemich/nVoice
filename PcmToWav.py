import wave

def convert(name, auido_name):
    with open(name, 'rb') as pcmfile:
        pcmdata = pcmfile.read()

    with wave.open(auido_name, 'wb') as f:
        f.setparams((1, 2, 44100, 1, 'NONE', 'NONE'))
        f.writeframes(pcmdata)
        