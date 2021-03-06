import soundfile as sf
import os


def len_audio(path):
    wav, sr = sf.read(path)
    return len(wav) // sr


if __name__ == '__main__':
    with open('len.txt', 'w') as f:
        for fname in os.listdir('data'):
            f.write(str(len_audio(fname)) + '\n')
