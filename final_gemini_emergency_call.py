import speech_recognition as sr
from playsound import playsound
import time
import os
from facetime_call import fully_automated_facetime_call
import tkinter as tk
from tkinter import simpledialog
import requests
import json

# Path to alarm sound file (replace with your own sound file)
ALARM_SOUND = "alarm.wav"  # Make sure this file exists or replace with another audio file

# Global variables for user inputs
selected_phrase = "i want a cookie"
selected_contact = "+14085909699"
GEMINI_API_KEY = "AIzaSyC-GlpV2FS_wTSzqU3GlVu8G0AbkKCZrOE"  # Replace this with your actual API key

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

def analyze_with_gemini(text):
    """
    Analyzes the transcribed text using Google's Gemini API.
    Returns the analysis results.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    
    # Create a prompt that asks Gemini to analyze the text
    prompt = f"""
    Analyze the following transcribed speech and determine:
    1. The overall sentiment (positive, negative, neutral)
    2. If there are any concerning elements or urgent requests
    3. The main topic or intention
    
    Transcribed text: "{text}"
    
    Provide a brief analysis.
    """
    
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        
        # Extract the text from the response
        if 'candidates' in result and len(result['candidates']) > 0:
            if 'content' in result['candidates'][0] and 'parts' in result['candidates'][0]['content']:
                for part in result['candidates'][0]['content']['parts']:
                    if 'text' in part:
                        return part['text']
        
        return "Could not extract analysis from Gemini response."
    except Exception as e:
        return f"Error analyzing with Gemini: {e}"

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
                
                # Analyze the text with Gemini
                analysis = analyze_with_gemini(text)
                print("Gemini Analysis:")
                print(analysis)
                
                # Check for target phrase
                if selected_phrase in text:
                    print("Trigger phrase detected! Sounding alarm!")
                    trigger_alarm(text, analysis)
                    
        except sr.WaitTimeoutError:
            print("Listening timeout, continuing...")
            continue
        except sr.UnknownValueError:
            print("Could not understand audio, continuing...")
            continue
        except Exception as e:
            print(f"Error occurred: {e}")
            continue

def trigger_alarm(text, analysis):
    global selected_contact
    # Play alarm sound
    try:
        # playsound(ALARM_SOUND)
        # Include the analysis in the call or notification
        print(f"Making FaceTime call to {selected_contact}")
        print(f"Analysis to share: {analysis}")
        fully_automated_facetime_call(selected_contact)
    except Exception as e:
        print(f"Could not trigger alarm properly: {e}")
        # Fallback to system beep if audio file fails
        for _ in range(5):
            print('\a')  # System beep
            time.sleep(0.5)
    
    # You can add other alarm methods here like sending emails, showing popups
    # Example using Windows popup with the analysis:
    message = f"ALARM TRIGGERED!\nDetected phrase: {selected_phrase}\n\nAnalysis: {analysis}"
    try:
        os.system(f'msg * "{message}"')
    except:
        print("Could not show system message")

if __name__ == "__main__":
    get_user_inputs()
    listen_for_phrase()