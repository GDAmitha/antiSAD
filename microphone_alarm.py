import speech_recognition as sr
from playsound import playsound
import time
import os
from facetime_call import fully_automated_facetime_call
import tkinter as tk
from tkinter import simpledialog

# Path to alarm sound file (replace with your own sound file)
ALARM_SOUND = "alarm.wav"  # Make sure this file exists or replace with another audio file

# Global variables for user inputs
selected_phrase = "i want a cookie"
selected_contact = "+14085909699"

def get_user_inputs():
    global selected_phrase, selected_contact

    # Create a simple GUI for user input
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask for the trigger phrase
    selected_phrase = simpledialog.askstring("Input", "Enter the trigger phrase:", initialvalue=selected_phrase)
    if not selected_phrase:
        selected_phrase = "i want a cookie"  # Default value

    # Ask for the contact number
    selected_contact = simpledialog.askstring("Input", "Enter the contact number:", initialvalue=selected_contact)
    if not selected_contact:
        selected_contact = "+14085909699"  # Default value

def listen_for_phrase():
    global selected_phrase
    # Initialize recognizer
    r = sr.Recognizer()
    
    print("Program started, listening to microphone...")
    print(f"Waiting for phrase: '{selected_phrase}'")
    
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
                if selected_phrase in text:
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
    global selected_contact
    # Play alarm sound
    try:
        # playsound(ALARM_SOUND)
        fully_automated_facetime_call(selected_contact)

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
    get_user_inputs()
    listen_for_phrase()