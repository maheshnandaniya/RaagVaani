# 🎶 Raagvaani – Indian AI Music Generator

**Raagvaani** is an AI-powered song generation tool that brings the soul of Indian music into the world of AI. It allows users to generate full songs — lyrics, vocals, and background music — in popular Indian styles like **Hindi**, **Bollywood**, **Punjabi**, **Haryanvi**, **Marwari** and so on.

---

## 🌟 Features

- 🎤 Generate lyrics from a simple prompt
- 🗣️ AI-generated singing vocals (Bark / Coqui)
- 🥁 Instrumental music via MusicGen
- 🧠 Multilingual and regional genre support
- 🎧 Audio output rendered and playable
- 🖥️ Django web interfaes 

## 🛠️ Tech Stack

| Component         | Technology                  |
|------------------|-----------------------------|
| Backend           | Django (Python)             |
| AI Models         | Bark, Coqui TTS, MusicGen   |
| Audio Processing  | FFmpeg, torchaudio          |
| UI                | HTML + CSS + Django Forms   |
| Hosting (future)  | Streamlit / Docker / Cloud  |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/maheshnandaniya/Raagvaani.git
cd Raagvaani
pip install -r requirements.txt
python manage.py runserver
