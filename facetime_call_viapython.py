# # # import os
# # # import subprocess

# # # def open_facetime():
# # #     """
# # #     Opens the FaceTime application on macOS.
# # #     """
# # #     try:
# # #         # Using the 'open' command which is native to macOS
# # #         subprocess.run(['open', '-a', 'FaceTime'], check=True)
# # #         print("FaceTime has been opened successfully!")
# # #         return True
# # #     except subprocess.CalledProcessError as e:
# # #         print(f"Error opening FaceTime: {e}")
# # #         return False
# # #     except Exception as e:
# # #         print(f"An unexpected error occurred: {e}")
# # #         return False

# # # if __name__ == "__main__":
# # #     # Check if running on macOS
# # #     if os.name != 'posix' or not os.path.exists('/Applications/FaceTime.app'):
# # #         print("This script is designed for macOS and requires FaceTime to be installed.")
# # #     else:
# # #         open_facetime()

# # import os
# # import subprocess

# # def open_facetime():
# #     """
# #     Opens the FaceTime application on macOS.
# #     """
# #     try:
# #         # Using the 'open' command which is native to macOS
# #         subprocess.run(['open', '-a', 'FaceTime'], check=True)
# #         print("FaceTime has been opened successfully!")
# #         return True
# #     except subprocess.CalledProcessError as e:
# #         print(f"Error opening FaceTime: {e}")
# #         return False
# #     except Exception as e:
# #         print(f"An unexpected error occurred: {e}")
# #         return False

# # if __name__ == "__main__":
# #     # Check if running on macOS - we won't check for the exact path
# #     # since the 'open -a' command should find FaceTime regardless
# #     if os.name != 'posix':
# #         print("This script is designed for macOS.")
# #     else:
# #         open_facetime()


# import os
# import subprocess
# import sys

# def open_facetime_with_contact(contact=None):
#     """
#     Opens the FaceTime application on macOS.
#     If a contact is provided, initiates a call to that contact.
    
#     Args:
#         contact (str): Phone number (with country code) or email address to call
#     """
#     try:
#         if contact:
#             # Format for phone numbers: use facetime:// protocol with the number
#             # For emails: use facetime:// protocol with the email
#             # Strip any spaces or special characters from phone numbers
#             clean_contact = ''.join(c for c in contact if c.isalnum() or c == '@' or c == '.')
            
#             # Check if it's an email (contains @)
#             if '@' in clean_contact:
#                 facetime_url = f"facetime://{clean_contact}"
#             else:
#                 # Assume it's a phone number - add + if not present for country code
#                 if not clean_contact.startswith('+'):
#                     clean_contact = '+' + clean_contact
#                 facetime_url = f"facetime://{clean_contact}"
            
#             # Open FaceTime with the contact
#             subprocess.run(['open', facetime_url], check=True)
#             print(f"Initiating FaceTime call to {contact}")
#         else:
#             # Just open FaceTime without calling anyone
#             subprocess.run(['open', '-a', 'FaceTime'], check=True)
#             print("FaceTime has been opened successfully!")
        
#         return True
#     except subprocess.CalledProcessError as e:
#         print(f"Error opening FaceTime: {e}")
#         return False
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
#         open_facetime_with_contact(contact)
#     else:
#         # Ask for input if no command line argument
#         choice = input("Do you want to call someone? (y/n): ").lower()
#         if choice == 'y' or choice == 'yes':
#             contact = input("Enter phone number (with country code) or email: ")
#             open_facetime_with_contact(contact)
#         else:
#             open_facetime_with_contact()  # Just open FaceTime


import os
import subprocess
import sys
import re

def open_facetime_with_contact(contact=None):
    """
    Opens the FaceTime application on macOS.
    If a contact is provided, initiates a call to that contact.
    
    Args:
        contact (str): Phone number (with country code) or email address to call
    """
    try:
        if contact:
            # Check if it's an email
            if '@' in contact and re.match(r"[^@]+@[^@]+\.[^@]+", contact):
                # Just use the email as-is
                facetime_url = f"facetime:{contact}"
            else:
                # Format phone number - remove all non-digits except + at beginning
                phone = re.sub(r'[^\d+]', '', contact)
                if not phone.startswith('+'):
                    # Add + if not present for international format
                    phone = '+' + phone
                facetime_url = f"facetime:{phone}"
            
            print(f"Attempting to call: {facetime_url}")
            
            # First open FaceTime app to ensure it's running
            subprocess.run(['open', '-a', 'FaceTime'], check=True)
            
            # Wait a moment for FaceTime to initialize
            import time
            time.sleep(2)
            
            # Then open the URL
            subprocess.run(['open', facetime_url], check=True)
            print(f"Initiating FaceTime call to {contact}")
        else:
            # Just open FaceTime without calling anyone
            subprocess.run(['open', '-a', 'FaceTime'], check=True)
            print("FaceTime has been opened successfully!")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error with FaceTime: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    # Check if running on macOS
    if os.name != 'posix':
        print("This script is designed for macOS.")
        sys.exit(1)
    
    # Get contact from command line argument if provided
    if len(sys.argv) > 1:
        contact = sys.argv[1]
        open_facetime_with_contact(contact)
    else:
        # Ask for input if no command line argument
        choice = input("Do you want to call someone? (y/n): ").lower()
        if choice == 'y' or choice == 'yes':
            contact = input("Enter phone number (with country code) or email: ")
            open_facetime_with_contact(contact)
        else:
            open_facetime_with_contact()  # Just open FaceTime