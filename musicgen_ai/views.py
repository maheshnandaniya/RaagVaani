import os
import openai
from django.shortcuts import render
from django.conf import settings
from dotenv import load_dotenv
from .bark_wrapper import generate_bark_audio
from .musicgen_wrapper import generate_music
from .audio_mixer import merge_audio_tracks

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

        # Step 3: TODO – Convert lyrics to vocals using Bark (Coming next)
        # Generate Music
        music_path = f"media/{uuid.uuid4().hex}_music"
        music_output = generate_music(f"{genre} instrumental {prompt}", output_path=music_path)
        # Bark audio generation code will go here later
        voice = request.POST.get("voice", "female")

    # Map to Bark's speaker preset
    speaker_map = {
        "female": "v2/en_speaker_6",
        "male": "v2/en_speaker_1"
    }

    selected_speaker = speaker_map.get(voice, "v2/en_speaker_6")
        # For now, use dummy placeholder or skip

        # Step 4: Dummy test file for now
        audio_url = "/" + final_audio

        return render(request, "index.html", {
            "audio_url": audio_url,
            "lyrics": lyrics,
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
