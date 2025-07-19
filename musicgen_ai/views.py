import os
import openai
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from dotenv import load_dotenv
from .bark_wrapper import generate_bark_audio
from .musicgen_wrapper import generate_music
from .audio_mixer import merge_audio_tracks
from .tortoise_wrapper import generate_tortoise_audio

voice_presets = {
    "v2/en_speaker_0": "Neha AI",
    "v2/en_speaker_1": "Kishore AI",
    "v2/en_speaker_2": "Sunidhi AI",
    "v2/en_speaker_3": "RaagBot Bass",
    "v2/en_speaker_4": "Shaan AI",
    "v2/en_speaker_5": "Arijit AI",
    "v2/en_speaker_6": "Lata AI",
    "v2/en_speaker_7": "Diljit AI",
    "v2/en_speaker_8": "RaagBot Female",
    "v2/en_speaker_9": "Shreya AI",
    "v2/en_speaker_10": "Rafi AI",
    "v2/en_speaker_11": "Alka AI"
}

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def index(request):
    audio_url = None

    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        genre = request.POST.get("genre", "")

        # Step 1: Generate lyrics from prompt
        lyrics = generate_lyrics(prompt, genre)

        # Step 2: Save lyrics to .txt for reference (optional)
        with open("last_lyrics.txt", "w", encoding="utf-8") as f:
            f.write(lyrics)
        voice_model = request.POST.get("voice_model", "bark")  # default: bark

        if voice_model == "bark":
           audio_path = generate_bark_audio(lyrics, output_path=output_filename, speaker=voice)
        elif voice_model == "tortoise":
           audio_path = generate_tortoise_audio(lyrics, output_path=output_filename, voice="pat")
        else:
           audio_path = generate_bark_audio(lyrics, output_path=output_filename, speaker=voice)  # fallback

        # Step 3: TODO – Convert lyrics to vocals using Bark (Coming next)
        # Generate Music
        music_path = f"media/{uuid.uuid4().hex}_music"
        music_output = generate_music(f"{genre} instrumental {prompt}", output_path=music_path)
        # Bark audio generation code will go here later
        voice = request.POST.get("voice", "female")

    # Map to Bark's speaker preset
    voice = request.POST.get("voice", "v2/en_speaker_6")  # default: Lata AI
selected_voice_name = voice_presets.get(voice, "Lata AI")

        # Step 4: Dummy test file for now
        audio_url = "/" + final_audio

        return render(request, "index.html", {
    "lyrics": lyrics,
    "audio_url": audio_url,
    "selected_voice_name": selected_voice_name,
    "voice_presets": voice_presets  #Pass all to template
})

    return render(request, "index.html")
    
def generate_lyrics(prompt, genre):
    full_prompt = f"Write a {genre} song in Hindi (4 to 6 lines) based on the theme: {prompt}. Use poetic Bollywood style."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=200,
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()


final_audio = f"media/{uuid.uuid4().hex}_final.wav"
merge_audio_tracks(audio_path, music_output, final_audio)


def preview_voice(request):
    voice = request.GET.get("voice")
    name = voice_presets.get(voice, "This singer")

    line = f"Hello Raagvaani, I'm {name.replace(' AI', '')} and this is my voice."
    preview_file = f"media/previews/{name.replace(' ', '_')}.wav"

    if not os.path.exists(preview_file):
        generate_bark_audio(line, output_path=preview_file, speaker=voice)

    return JsonResponse({"audio_url": "/" + preview_file})
