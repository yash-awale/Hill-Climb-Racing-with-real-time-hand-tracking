import pyautogui
import time

print("Focus the game window... Starting in 5 seconds")
time.sleep(5)

print("Holding RIGHT key for 3 seconds...")
pyautogui.keyDown('right')
time.sleep(3)
pyautogui.keyUp('right')
print("Released RIGHT key")
