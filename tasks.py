import webbrowser
import pyautogui
import subprocess
import screen_brightness_control as bc
import platform
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
import pythoncom
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from urllib.parse import quote_plus

def startMSWord():
    """Attempts to open the Microsoft Word application and handles errors in case the attempt fails."""
    try:
        subprocess.Popen(['start', 'winword'], shell=True)
        return "Attempting to open Microsoft Word."
    except FileNotFoundError:
        return "Failed to launch Microsoft Word as the application could not be located."
    except Exception as e:
        return f"Failed to open Microsoft Word: {e}"

screenshot_counter = 1
def screenshot():
    """ Captures and saves a screenshot, then returns the filename. """
    global screenshot_counter
    filename = f"screenshot{screenshot_counter}.png"
    screenshot_img = pyautogui.screenshot()
    screenshot_img.save(filename)
    screenshot_counter += 1
    return f"Screenshot saved as {filename}"

def google_search(search_item):
    """ Opens the default web browser and searches Google with the given search item. Returns a message after the search has been initiated." """
    webbrowser.open(f"https://www.google.com/search?q={search_item}")
    return f"Searching Google for '{search_item}'."

def youtube_search(search_item):
    """ Opens the default web browser and searches YouTube with the given query. Returns a message after the search has been initiated. """
    encoded_search_item = quote_plus(search_item)
    webbrowser.open(f"https://www.youtube.com/results?search_query={encoded_search_item}")
    return f"Searching YouTube for '{search_item}'."

def download_music():
    """Placeholder function for the download music command since we were not required to fully implement it."""
    return "Download music command/feature is a placeholder for now."


if platform.system() != "Windows":
    raise EnvironmentError("This volume control utility is designed for Windows only.")

def get_master_volume_object():
    """ Retrieves the system's master volume object using PyCAW.  """
    try:
        pythoncom.CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        return cast(interface, POINTER(IAudioEndpointVolume))
    except Exception as e:
        print(f"ERROR in get_master_volume_object: {e}")
        return None

def get_volume_percentage():
    """ Returns the current system volume as a percentage (0-100). """
    volume = get_master_volume_object()
    if volume:
        try:
            scalar = volume.GetMasterVolumeLevelScalar()
            return int(round(scalar * 100))
        except Exception as e:
            print(f"Error getting scalar volume: {e}")
    return None

def set_volume_percentage(percentage):
    """ Sets the system volume to a specific percentage (0-100). """
    if not 0 <= percentage <= 100:
        return "Percentage must be between 0 and 100."
    volume = get_master_volume_object()
    if volume:
        try:
            volume.SetMasterVolumeLevelScalar(percentage / 100.0, None)
            return f"Volume set to {percentage}%."
        except Exception as e:
            return f"Failed to set volume: {e}"
    return "Failed to access Windows audio device."

def high_volume(step=10):
    """ Increases the system volume by a given step, capped at 100%. """
    current = get_volume_percentage()
    if current is not None:
        new_vol = min(100, current + step)
        return set_volume_percentage(new_vol)
    return "Failed to get current volume."

def low_volume(step=10):
    """ Decreases the system volume by a given step, capped at 0%. """
    current = get_volume_percentage()
    if current is not None:
        new_vol = max(0, current - step)
        return set_volume_percentage(new_vol)
    return "Failed to get current volume."

def mute():
    """ Mutes the system audio. """
    volume = get_master_volume_object()
    if volume:
        try:
            volume.SetMute(1, None)
            return "System muted."
        except Exception as e:
            return f"Failed to mute: {e}"
    return "Failed to access Windows audio device."

def unmute():
    """ Unmutes the system audio. """
    volume = get_master_volume_object()
    if volume:
        try:
            volume.SetMute(0, None)
            return "System unmuted."
        except Exception as e:
            return f"Failed to unmute: {e}"
    return "Failed to access Windows audio device."

def get_brightness():
    """ Retrieves the system's screen brightness object. """
    try:
        current = bc.get_brightness(display=0)
        return current[0] if isinstance(current, list) else current
    except Exception as e:
        print(f"Error getting brightness: {e}")
        return None

def set_brightness(value):
    """ Sets the system's screen brightness to desired value. """
    try:
        bc.set_brightness(value, display=0)
        return f"Brightness set to {value}%."
    except Exception as e:
        return f"Failed to set brightness: {e}"

def lower_brightness(step=10):
    """ Decreases the system screen brightness by a step of 10, capped at 0%. """
    current = get_brightness()
    if current is not None:
        new_brightness = max(current - step, 0)
        return set_brightness(new_brightness)
    return "Failed to get current brightness."

def higher_brightness(step=10):
    """ Increases the system screen brightness by a step of 10, capped at 0%. """
    current = get_brightness()
    if current is not None:
        new_brightness = min(current + step, 100)
        return set_brightness(new_brightness)
    return "Failed to get current brightness."

