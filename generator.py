import numpy as np
import sounddevice as sd

def zzfx(
    frequency=440.0,
    shape='sine',
    duration=0.5,
    drive=1.0,
    sample_rate=44100
):

    total_samples = int(duration * sample_rate)
    time_arr = np.linspace(0, duration, num=total_samples, endpoint=False)
    

    phase_arr = 2 * np.pi * frequency * time_arr
    

    if shape == 'sine':
        wave = np.sin(phase_arr)
    elif shape == 'square':
        wave = np.sign(np.sin(phase_arr))
    elif shape == 'sawtooth':
        wave = 2.0 * (phase_arr / (2 * np.pi) - np.floor(0.5 + phase_arr / (2 * np.pi)))
    elif shape == 'triangle':
        wave = 2.0 * np.abs(2.0 * (phase_arr / (2 * np.pi) - np.floor(phase_arr / (2 * np.pi) + 0.5))) - 1.0
    elif shape == 'white':
        wave = np.random.uniform(-1.0, 1.0, size=total_samples)
    else:
        wave = np.sin(phase_arr)

    if drive > 1.0:
        wave = np.tanh(wave * drive)


    max_val = np.max(np.abs(wave))
    if max_val > 0:
        wave = wave / max_val

    return wave, sample_rate

def play_audio(audio_data, sample_rate=44100):
    sd.play(audio_data, samplerate=sample_rate)
    sd.wait()

if __name__ == '__main__':
    audio, sr = zzfx(frequency=220, shape='sawtooth', drive=3.0)
    play_audio(audio, sr)