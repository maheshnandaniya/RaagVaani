from bark import SAMPLE_RATE, generate_audio
import soundfile as sf

def generate_bark_audio(lyrics_text, output_path="bark_output.wav"):
    audio_array = generate_audio(lyrics_text)
    sf.write(output_path, audio_array, SAMPLE_RATE)
    return output_path
