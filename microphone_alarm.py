# import speech_recognition as sr
# from playsound import playsound
# import time
# import os
# from facetime_call import fully_automated_facetime_call
# import tkinter as tk
# from tkinter import simpledialog
# import gemini  # Assuming Gemini has a Python SDK
# from google.cloud import speech
# import google.generativeai as genai


# # Path to alarm sound file (replace with your own sound file)
# ALARM_SOUND = "alarm.wav"  # Make sure this file exists or replace with another audio file

# # Global variables for user inputs
# selected_phrase = "i want a cookie"
# selected_contact = "+14085909699"

# def get_user_inputs():
#     global selected_phrase, selected_contact

#     # Create a simple GUI for user input
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window

#     # Ask for the trigger phrase
#     selected_phrase = simpledialog.askstring("Input", "Enter the trigger phrase:", initialvalue=selected_phrase)
#     if not selected_phrase:
#         selected_phrase = "i want a cookie"  # Default value

#     # Ask for the contact number
#     selected_contact = simpledialog.askstring("Input", "Enter the contact number:", initialvalue=selected_contact)
#     if not selected_contact:
#         selected_contact = "+14085909699"  # Default value

# # def transcribe_audio_with_gemini(audio_file_path):
# #     """
# #     Transcribes audio using Gemini's transcription service.
# #     """
# #     try:
# #         # Initialize Gemini client (replace with actual initialization code)
# #         client = gemini.Client(api_key="AIzaSyC-GlpV2FS_wTSzqU3GlVu8G0AbkKCZrOE")  # Replace with your API key
# #         response = client.transcribe(audio_file_path)
# #         return response.get("transcription", "").lower()
# #     except Exception as e:
# #         print(f"Gemini transcription error: {e}")
# #         return ""


# def transcribe_audio_with_google(audio_file_path):
#     """
#     Transcribes audio using Google's Speech-to-Text API.
#     """
#     try:
#         # Initialize Speech-to-Text client
#         client = speech.SpeechClient()
        
#         # Read the audio file
#         with open(audio_file_path, "rb") as audio_file:
#             content = audio_file.read()
        
#         # Configure the audio settings
#         audio = speech.RecognitionAudio(content=content)
#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=16000,
#             language_code="en-US",
#         )
        
#         # Perform the transcription
#         response = client.recognize(config=config, audio=audio)
        
#         # Extract and return the transcript
#         transcript = ""
#         for result in response.results:
#             transcript += result.alternatives[0].transcript
        
#         return transcript.lower()
#     except Exception as e:
#         print(f"Google Speech-to-Text error: {e}")
#         return ""

# def listen_for_phrase():
#     global selected_phrase
#     # Initialize recognizer
#     r = sr.Recognizer()
    
#     print("Program started, listening to microphone...")
#     print(f"Waiting for phrase: '{selected_phrase}'")
    
#     while True:
#         try:
#             # Use microphone as audio source
#             with sr.Microphone() as source:
#                 # Adjust for ambient noise
#                 r.adjust_for_ambient_noise(source, duration=0.5)
#                 print("Listening...")
#                 # Listen to audio input
#                 audio = r.listen(source, timeout=5, phrase_time_limit=5)
                
#                 # Save audio to a temporary file
#                 with open("temp_audio.wav", "wb") as f:
#                     f.write(audio.get_wav_data())
                
#                 # Use Gemini for transcription
#                 text = transcribe_audio_with_gemini("temp_audio.wav")
#                 print(f"Recognized: {text}")
                
#                 # Check for target phrase
#                 if selected_phrase in text:
#                     print("Trigger phrase detected! Sounding alarm!")
#                     trigger_alarm()
                    
#         except sr.WaitTimeoutError:
#             print("Listening timeout, continuing...")
#             continue
#         except Exception as e:
#             print(f"Error occurred: {e}")
#             continue

# def trigger_alarm():
#     global selected_contact
#     # Play alarm sound
#     try:
#         # playsound(ALARM_SOUND)
#         fully_automated_facetime_call(selected_contact)

#     except:
#         print("Could not play alarm sound, using system beep")
#         # Fallback to system beep if audio file fails
#         for _ in range(5):
#             print('\a')  # System beep
#             time.sleep(0.5)
    
#     # You can add other alarm methods here like sending emails, showing popups
#     # Example using Windows popup:
#     os.system('msg * "ALARM TRIGGERED! Detected phrase: I want a cookie"')

# if __name__ == "__main__":
#     get_user_inputs()
#     listen_for_phrase()

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