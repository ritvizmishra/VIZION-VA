import speech_recognition as sr
import pyttsx3
import webbrowser
import music_lib
import requests
import wikipedia
from bs4 import BeautifulSoup

# initialize pyttsx3 module.
engine = pyttsx3.init()
newsapi = "64e17ca2886a49739c5fcb3aeabe4cc6"

# create a function for speaking.
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# fetch DuckDuckGo summary
def fetch_duckduckgo_summary(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    res = requests.get(url)
    data = res.json()
    summary = data.get("Abstract")
    if summary:
        speak(summary)
        return True
    return False

# fetch wikipedia summary
def fetch_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
        return True
    except:
        return False
    
# google snippet scraping
def fetch_google_snippet(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        snippet = soup.find("div", class_="BNeawe s3v9rd AP7Wnd").text
        speak(f"According to Google: {snippet}")
        return True
    except:
        return False
    
# create fallback query handler
def fallback_query_handler(query):
    if fetch_duckduckgo_summary(query):
        return
    elif fetch_wikipedia_summary(query):
        return
    elif fetch_google_snippet(query):
        return
    else:
        speak("I couldn't find an answer. Let me open it on Google for you.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
# create a function to process commands given by the user
def processCommand(command):
    command_lower = command.lower()
    
    # deactivating vizion
    if "go to sleep" in command_lower:
        speak("Goodbye friend, see you soon!")
        
    # open website asked by the user
    elif "open google" in command_lower:
        speak("Opening Google...")
        webbrowser.open("https://google.com")
    elif "open youtube" in command_lower:
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command_lower:
        speak("Opening LinkedIN...")
        webbrowser.open("https://linkedin.com")
    elif "open github" in command_lower:
        speak("Opening GitHub...")
        webbrowser.open("https://github.com")
    elif "open spotify" in command_lower:
        speak("Opening Spotify...")
        webbrowser.open("https://spotify.com")
        
    # play songs on YT using pywhatkit
    elif command_lower.startswith("play"):
        # play song requested
        song = command_lower
        music_lib.music(song)
        
        # remove play from the beginning
        song = command_lower.replace("play", "", 1).strip()
        # remove trailing "on youtube" if user says it
        if song.endswith("on youtube"):
            song = song.replace("on youtube", "").strip()
        speak(f"Playing {song} on YouTube...")
    
    # add news feature:
    elif "news" in command_lower or "headlines" in command_lower:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            speak("Here are the top headlines.")
            for idx, article in enumerate(articles[:5], 1):
                speak(f"{idx}. {article.get('title')}")
        else:
            speak("Failed to fetch news.")
            
    else:
        speak("Let me search that for you.")
        fallback_query_handler(command)
        
# prevent unintended code execution.
if __name__ == "__main__":
    
    # set up activation message for Vizion
    speak("Waking up Vision...") 
    while True:
        # obtain audio from the microphone and activate Vizion
        r = sr.Recognizer()

        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening to you...")
                audio = r.listen(source)
                word = r.recognize_google(audio) 
            print("\nRecognizing...")
            
            # wake-up Vizion when activation requested
            if 'vision' in word.lower():
                # take the command from the user
                with sr.Microphone() as source:
                    print("\nVizion Active...")
                    speak("Yes, how can I help you?")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    print("\nRecognizing...")
                    
                    # process the command given
                    processCommand(command)
                    
            # deactivate Vizion
            elif "go to sleep" in word.lower():
                speak("Goodbye friend, see you soon!")
                break        
        except Exception as e:
            speak("Vision could not understand the audio.")
