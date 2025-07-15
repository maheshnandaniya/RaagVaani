import os
import openai
from django.shortcuts import render
from django.conf import settings
from dotenv import load_dotenv
from .bark_wrapper import generate_bark_audio

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
        # Bark audio generation code will go here later
        # For now, use dummy placeholder or skip

        # Step 4: Dummy test file for now
        audio_url = "/static/sample.mp3"

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
