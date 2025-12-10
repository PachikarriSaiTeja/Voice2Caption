import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

DURATION = 5  


INPUT_DEVICE_INDEX = 1

def record_audio():

    device_info = sd.query_devices(INPUT_DEVICE_INDEX, 'input')
    sample_rate = int(device_info['default_samplerate'])

    print(f"Using input device {INPUT_DEVICE_INDEX}: {device_info['name']}")
    print(f"Default sample rate: {sample_rate} Hz")
    print(f"Recording for {DURATION} seconds...")


    sd.default.device = (INPUT_DEVICE_INDEX, None)

    audio = sd.rec(
        int(DURATION * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='float32'
    )
    sd.wait()
    print("Recording complete.")

    print("Volume range:", float(audio.min()), float(audio.max()))
    return audio, sample_rate

if __name__ == "__main__":
    audio, sr = record_audio()

    
    audio_int16 = np.int16(audio * 32767)
    wav.write("test_recording.wav", sr, audio_int16)
    print(f"Saved to test_recording.wav at {sr} Hz — play it and check sound.")
