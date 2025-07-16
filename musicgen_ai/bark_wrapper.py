from bark import SAMPLE_RATE, generate_audio
import soundfile as sf

def generate_bark_audio(lyrics_text, output_path="bark_output.wav", speaker="v2/en_speaker_6"):
    audio_array = generate_audio(lyrics_text, history_prompt=speaker)
    sf.write(output_path, audio_array, SAMPLE_RATE)
    return output_path
