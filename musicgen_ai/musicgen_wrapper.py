import torch
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

# Load model once
model = MusicGen.get_pretrained('melody')

def generate_music(prompt, output_path="musicgen_output"):
    model.set_generation_params(duration=10)  # seconds
    music = model.generate([prompt])
    audio_write(output_path, music[0].cpu(), model.sample_rate, format="wav")
    return output_path + ".wav"
