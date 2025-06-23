import pyautogui
import time

print("👉 Move your mouse to the GAS button in 5 seconds...")
time.sleep(5)

pos = pyautogui.position()
print("🧭 Your GAS button position is:", pos)
