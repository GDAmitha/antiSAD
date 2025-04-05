import speech_recognition as sr
from playsound import playsound
import time
import os

# Path to alarm sound file (replace with your own sound file)
ALARM_SOUND = "alarm.wav"  # Make sure this file exists or replace with another audio file

def listen_for_phrase():
    # Initialize recognizer
    r = sr.Recognizer()
    
    print("Program started, listening to microphone...")
    print("Waiting for phrase: 'I want a cookie'")
    
    while True:
        try:
            # Use microphone as audio source
            with sr.Microphone() as source:
                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                # Listen to audio input
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                
                # Use Google speech recognition
                text = r.recognize_google(audio).lower()
                print(f"Recognized: {text}")
                
                # Check for target phrase
                if "i want a cookie" in text:
                    print("Trigger phrase detected! Sounding alarm!")
                    trigger_alarm()
                    
        except sr.WaitTimeoutError:
            print("Listening timeout, continuing...")
            continue
        except sr.UnknownValueError:
            print("Could not understand audio, continuing...")
            continue
        except Exception as e:
            print(f"Error occurred: {e}")
            continue

def trigger_alarm():
    # Play alarm sound
    try:
        playsound(ALARM_SOUND)
    except:
        print("Could not play alarm sound, using system beep")
        # Fallback to system beep if audio file fails
        for _ in range(5):
            print('\a')  # System beep
            time.sleep(0.5)
    
    # You can add other alarm methods here like sending emails, showing popups
    # Example using Windows popup:
    os.system('msg * "ALARM TRIGGERED! Detected phrase: I want a cookie"')

if __name__ == "__main__":
    listen_for_phrase()