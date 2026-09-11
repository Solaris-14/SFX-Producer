import numpy as np
import sounddevice as sd

def gen_time_array(duration, sample_rate = 44100):
    total_samples = int(duration*sample_rate)
    time_arr = np.linspace(0,duration, num = total_samples, endpoint = False)
    return time_arr

def generate_waveform(time_arr, frequency, shape = 'sine'):
    phase_arr = 2*np.pi*frequency*time_arr
    if shape == 'sine':
        return np.sin(phase_arr)
    if shape == 'square':
        return np.sign(np.sin(phase_arr))
    if shape == 'sawtooth':
        return 2.0 * (phase_arr / (2 * np.pi) - np.floor(0.5 + phase_arr / (2 * np.pi)))
    if shape == 'white':
        return np.random.uniform(-1.,1, size = len(time_arr))

def play_audio(audio_data, sample_rate=44100):
    





