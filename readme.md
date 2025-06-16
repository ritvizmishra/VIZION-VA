# VIZION-VA

![VIZION Banner](https://socialify.git.ci/ritvizmishra/VIZION-VA/image?language=1&name=1&owner=1&theme=Light)

**VIZION** is a desktop-based voice-controlled virtual assistant built in Python. It can recognize your voice commands and perform tasks like opening websites, playing YouTube music, fetching news, and answering general queries with intelligent summaries from DuckDuckGo, Wikipedia, and Google Scrapping.

> I will be adding OpenAI's GPT-3.5-Turbo Model to this virtual assitant in the future for better and more accurate summaries.

---

## Features

- Voice-activated using “Vizion” as the wake word
- Plays music directly from YouTube using `pywhatkit`
- Opens popular websites like Google, YouTube, LinkedIn, GitHub, Spotify
- Fetches real-time news headlines using NewsAPI
- Answers queries using:
  - DuckDuckGo Instant Answer API
  - Wikipedia summary
  - Google Snippet scraping (fallback)
- Graphical User Interface (GUI) built with `Tkinter`

---

## Libraries Used

- `speech_recognition` – for recognizing spoken commands
- `pyttsx3` – for voice output (text-to-speech)
- `pywhatkit` – for YouTube song playback
- `requests` – for API access and web scraping
- `wikipedia` – for fetching summary info
- `bs4` (BeautifulSoup) – for parsing Google snippets
- `tkinter`, `ttk`, `Pillow` – for GUI

---

## APIs and Services

- **NewsAPI** – [https://newsapi.org](https://newsapi.org)  
  Used to fetch top US news headlines. Replace your key in `vizion_backend.py`:
  > Indian headlines are not available on NewsAPI.
  ```python
  newsapi = "your_api_key_here"
  ```
- **DuckDuckGo Instant Answer API**  
  Used to fetch quick summaries for fallback answers.

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ritvizmishra/VIZION-VA
cd VIZION-VA
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia requests beautifulsoup4 pillow
```

> For `speech_recognition` to work, make sure `pyaudio` is installed. If you face issues:
```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Run the Assistant

```bash
python vizion_frontend.py
```

Press **Esc** to exit full-screen mode.

---

## Project Structure

```
VIZION-VA/
├── vizion_frontend.py       # Tkinter GUI interface
├── vizion_backend.py        # Main voice logic & processing
├── music_lib.py             # YouTube music playback via pywhatkit
├── vizion_logo.png          # Optional branding image (used in GUI)
├── VIZION-VA.svg            # Socialify preview (for README)
└── requirements.txt         # Python dependencies
```

---

## Customization Tips

- Update or extend `processCommand()` in `vizion_backend.py` to handle more commands.
- Add additional APIs or voice responses as needed.
- Swap the wake word or activate on hotkey.
- Replace logo image: `vizion_logo.png` (150x150 preferred).

---

## Packaging as an Executable

To share with others without Python:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed vizion_frontend.py
```

Include assets like images in the build using `--add-data`.

---

## Author

Built with passion by [Ritviz Mishra](https://github.com/ritvizmishra)
