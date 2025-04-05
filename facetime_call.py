# # # import os
# # # import subprocess
# # # import sys
# # # import re
# # # import time

# # # def facetime_call_using_applescript(contact):
# # #     """
# # #     Uses AppleScript to fully automate a FaceTime call.
    
# # #     Args:
# # #         contact (str): Phone number or email to call
# # #     """
# # #     # Format the contact appropriately
# # #     if '@' in contact:
# # #         # It's an email
# # #         formatted_contact = contact
# # #     else:
# # #         # It's a phone number - clean it up
# # #         formatted_contact = re.sub(r'[^\d+]', '', contact)
# # #         if not formatted_contact.startswith('+'):
# # #             formatted_contact = '+' + formatted_contact
    
# # #     # Create AppleScript that:
# # #     # 1. Opens FaceTime
# # #     # 2. Waits for it to load
# # #     # 3. Clicks the "New FaceTime" button
# # #     # 4. Enters the contact information
# # #     # 5. Hits return/enter to start the call
# # #     applescript = f'''
# # #     tell application "FaceTime"
# # #         activate
# # #         delay 2
        
# # #         -- Press New FaceTime button (Command+N)
# # #         tell application "System Events"
# # #             keystroke "n" using {{command down}}
# # #             delay 1
            
# # #             -- Type the contact
# # #             keystroke "{formatted_contact}"
# # #             delay 1
            
# # #             -- Press return/enter to initiate the call
# # #             keystroke return
# # #         end tell
# # #     end tell
# # #     '''
    
# # #     try:
# # #         # Execute the AppleScript
# # #         process = subprocess.Popen(['osascript', '-e', applescript], 
# # #                                   stdout=subprocess.PIPE, 
# # #                                   stderr=subprocess.PIPE)
# # #         stdout, stderr = process.communicate()
        
# # #         if process.returncode == 0:
# # #             print(f"Successfully initiated FaceTime call to {contact}")
# # #             return True
# # #         else:
# # #             print(f"Error: {stderr.decode('utf-8')}")
# # #             return False
# # #     except Exception as e:
# # #         print(f"An unexpected error occurred: {e}")
# # #         return False

# # # if __name__ == "__main__":
# # #     # Check if running on macOS
# # #     if os.name != 'posix':
# # #         print("This script is designed for macOS.")
# # #         sys.exit(1)
    
# # #     # Get contact from command line argument if provided
# # #     if len(sys.argv) > 1:
# # #         contact = sys.argv[1]
# # #         facetime_call_using_applescript(contact)
# # #     else:
# # #         # Ask for input if no command line argument
# # #         contact = input("Enter phone number (with country code) or email to call: ")
# # #         facetime_call_using_applescript(contact)


# # import os
# # import subprocess
# # import sys
# # import re
# # import time

# # def facetime_call_using_applescript(contact, use_video=True):
# #     """
# #     Uses AppleScript to fully automate a FaceTime call.
    
# #     Args:
# #         contact (str): Phone number or email to call
# #         use_video (bool): Whether to initiate a video call (True) or audio-only call (False)
# #     """
# #     # Format the contact appropriately
# #     if '@' in contact:
# #         # It's an email
# #         formatted_contact = contact
# #     else:
# #         # It's a phone number - clean it up
# #         formatted_contact = re.sub(r'[^\d+]', '', contact)
# #         if not formatted_contact.startswith('+'):
# #             formatted_contact = '+' + formatted_contact
    
# #     # Create more advanced AppleScript that:
# #     # 1. Opens FaceTime
# #     # 2. Waits for it to load
# #     # 3. Clicks the "New FaceTime" button
# #     # 4. Enters the contact information
# #     # 5. Waits for contact to be recognized
# #     # 6. Clicks the video or audio call button
# #     applescript = f'''
# #     tell application "FaceTime"
# #         activate
# #         delay 2
        
# #         tell application "System Events"
# #             -- Press New FaceTime button (Command+N)
# #             keystroke "n" using {{command down}}
# #             delay 1
            
# #             -- Type the contact
# #             keystroke "{formatted_contact}"
# #             delay 2
            
# #             -- Press Tab to move to the buttons
# #             keystroke tab
# #             delay 0.5
            
# #             -- Press Tab again to reach the FaceTime button (this might need adjustment)
# #             keystroke tab
# #             delay 0.5
            
# #             -- Press Space to click the button
# #             keystroke space
# #         end tell
# #     end tell
# #     '''
    
# #     try:
# #         # Execute the AppleScript
# #         process = subprocess.Popen(['osascript', '-e', applescript], 
# #                                   stdout=subprocess.PIPE, 
# #                                   stderr=subprocess.PIPE)
# #         stdout, stderr = process.communicate()
        
# #         if process.returncode == 0:
# #             print(f"Successfully initiated FaceTime call to {contact}")
# #             return True
# #         else:
# #             print(f"Error: {stderr.decode('utf-8')}")
# #             return False
# #     except Exception as e:
# #         print(f"An unexpected error occurred: {e}")
# #         return False

# # if __name__ == "__main__":
# #     # Check if running on macOS
# #     if os.name != 'posix':
# #         print("This script is designed for macOS.")
# #         sys.exit(1)
    
# #     # Get contact from command line argument if provided
# #     if len(sys.argv) > 1:
# #         contact = sys.argv[1]
# #         # Check if video or audio-only flag is provided
# #         video_call = True
# #         if len(sys.argv) > 2 and sys.argv[2].lower() in ['audio', 'a', 'audio-only']:
# #             video_call = False
# #         facetime_call_using_applescript(contact, video_call)
# #     else:
# #         # Ask for input if no command line argument
# #         contact = input("Enter phone number (with country code) or email to call: ")
# #         call_type = input("Video call? (y/n): ").lower()
# #         video_call = call_type.startswith('y')
# #         facetime_call_using_applescript(contact, video_call)

# import os
# import subprocess
# import sys
# import re

# def facetime_call_fully_automated(contact):
#     """
#     Uses detailed AppleScript UI scripting to fully automate a FaceTime call.
    
#     Args:
#         contact (str): Phone number or email to call
#     """
#     # Format the contact appropriately
#     if '@' in contact:
#         # It's an email
#         formatted_contact = contact
#     else:
#         # It's a phone number - clean it up
#         formatted_contact = re.sub(r'[^\d+]', '', contact)
#         if not formatted_contact.startswith('+'):
#             formatted_contact = '+' + formatted_contact
    
#     # This AppleScript uses UI scripting to precisely locate and interact with UI elements
#     applescript = f'''
#     tell application "FaceTime" to activate
#     delay 2
    
#     tell application "System Events"
#         tell process "FaceTime"
#             # Click the New Call button
#             try
#                 click button "New FaceTime" of window 1
#             on error
#                 # Fallback if button not found - try keyboard shortcut
#                 keystroke "n" using {{command down}}
#             end try
            
#             delay 1.5
            
#             # Enter the contact info
#             keystroke "{formatted_contact}"
#             delay 1.5
            
#             # Try to locate and click the call button directly by name
#             try
#                 # Try to find and click the "FaceTime" button (video call)
#                 click button "FaceTime" of window 1
#             on error
#                 try
#                     # Try to click the video call button by another possible name
#                     click button "Video" of window 1
#                 on error
#                     try
#                         # Try to find buttons by UI hierarchy
#                         # This is a more advanced way to find the button if needed
#                         set callButtons to buttons of window 1 whose title contains "FaceTime" or title contains "Video" or title contains "Call"
#                         if length of callButtons > 0 then
#                             click item 1 of callButtons
#                         else
#                             # Last resort - tab to what should be the call button and press space
#                             keystroke tab
#                             keystroke tab
#                             keystroke space
#                         end if
#                     end try
#                 end try
#             end try
#         end tell
#     end tell
#     '''
    
#     try:
#         # Execute the AppleScript
#         process = subprocess.Popen(['osascript', '-e', applescript], 
#                                   stdout=subprocess.PIPE, 
#                                   stderr=subprocess.PIPE)
#         stdout, stderr = process.communicate()
        
#         if process.returncode == 0:
#             print(f"Successfully initiated FaceTime call to {formatted_contact}")
#             return True
#         else:
#             error = stderr.decode('utf-8')
#             print(f"Error: {error}")
            
#             # Provide troubleshooting suggestions
#             print("\nTroubleshooting suggestions:")
#             print("1. Make sure Terminal has Accessibility permissions in System Preferences")
#             print("2. Try running the script with sudo (requires password)")
#             print("3. Make sure the contact information is correct")
#             return False
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return False

# if __name__ == "__main__":
#     # Check if running on macOS
#     if os.name != 'posix':
#         print("This script is designed for macOS.")
#         sys.exit(1)
    
#     # Get contact from command line argument if provided
#     if len(sys.argv) > 1:
#         contact = sys.argv[1]
#         facetime_call_fully_automated(contact)
#     else:
#         # Ask for input if no command line argument
#         contact = input("Enter phone number (with country code) or email to call: ")
#         facetime_call_fully_automated(contact)

import os
import subprocess
import sys
import re

def fully_automated_facetime_call(contact):
    """
    Initiates a FaceTime call using a more direct Apple Events approach
    that should require no user interaction.
    
    Args:
        contact (str): Phone number or email to call
    """
    # Format the contact appropriately
    if '@' in contact:
        # It's an email
        formatted_contact = contact
    else:
        # It's a phone number - clean it up
        formatted_contact = re.sub(r'[^\d+]', '', contact)
        if not formatted_contact.startswith('+'):
            formatted_contact = '+' + formatted_contact
    
    # This AppleScript uses a direct approach to call the contact
    # with a fallback to UI scripting if needed
    applescript = f'''
    -- Try the direct approach first
    tell application "FaceTime"
        activate
        delay 1
    end tell
    
    -- Try to directly initiate the call via URL
    do shell script "open 'facetime://" & "{formatted_contact}" & "'"
    delay 1
    
    -- Fallback method using UI scripting
    tell application "System Events"
        tell process "FaceTime"
            -- If we need to navigate through buttons after the URL is opened
            delay 1
            -- Try to find and click any "Call" or "FaceTime" button that appears
            repeat 3 times
                try
                    set callButtons to buttons of window 1 whose name contains "FaceTime" or name contains "Call" or name contains "Video"
                    if length of callButtons > 0 then
                        click item 1 of callButtons
                        exit repeat
                    end if
                end try
                delay 0.5
            end repeat
            
            -- If buttons approach didn't work, try keyboard navigation
            try
                -- Press Return key which should initiate the call
                keystroke return
            end try
        end tell
    end tell
    '''
    
    try:
        # Execute the AppleScript
        process = subprocess.Popen(['osascript', '-e', applescript], 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            print(f"Successfully initiated FaceTime call to {formatted_contact}")
            return True
        else:
            error = stderr.decode('utf-8')
            print(f"Error: {error}")
            
            # Provide troubleshooting suggestions
            print("\nTroubleshooting suggestions:")
            print("1. Make sure Terminal has Accessibility permissions in System Preferences")
            print("2. Check if FaceTime is properly configured with your Apple ID")
            print("3. Make sure the contact information is correct")
            return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# if __name__ == "__main__":
#     # Check if running on macOS
#     if os.name != 'posix':
#         print("This script is designed for macOS.")
#         sys.exit(1)
    
#     # Get contact from command line argument if provided
#     if len(sys.argv) > 1:
#         contact = sys.argv[1]
#         fully_automated_facetime_call(contact)
#     else:
#         # Ask for input if no command line argument
#         contact = input("Enter phone number (with country code) or email to call: ")
#         fully_automated_facetime_call(contact)

# fully_automated_facetime_call('+14085909699')
