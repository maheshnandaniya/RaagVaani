# tortoise_wrapper.py

import os
from tortoise.api import TextToSpeech
import torchaudio

TORTOISE_PRESET_VOICE = "pat"  # You can change this or make it dynamic

tts = TextToSpeech()

def generate_tortoise_audio(text, output_path="tortoise_output.wav", voice=TORTOISE_PRESET_VOICE):
    """
    Generates AI singing/speaking using Tortoise TTS.
    """
    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Generate audio
    print(f"[Tortoise] Generating voice for: {voice}")
    gen = tts.tts(text, voice=voice, preset="high_quality")

    # Save as WAV
    torchaudio.save(output_path, gen.squeeze(0).cpu(), 24000)
    return output_path
