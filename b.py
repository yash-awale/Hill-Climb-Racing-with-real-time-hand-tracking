import pyautogui
import time

print("Move mouse to BRAKE button in 5 seconds...")
time.sleep(5)
print("Your BRAKE button position is:", pyautogui.position())
