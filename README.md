# 🚗 GestureDrive – Control Hill Climb Racing with Hand Gestures

This project lets you play the popular **Hill Climb Racing** PC game using just your **hand gestures** – no keyboard or mouse needed!  
Built using **Python**, **MediaPipe**, and **PyAutoGUI**, it detects your hand in real-time via webcam and translates gestures into game controls.

---

## 🎮 Live Game Controls

| Gesture       | Action            |
|---------------|-------------------|
| ✋ Open Hand  | Press GAS (Accelerate) |
| ✊ Closed Fist | Press BRAKE (Stop/Reverse) |

---

## 🔧 Technologies Used

- 🐍 Python 3.10  
- 📷 OpenCV (Webcam handling)  
- ✋ MediaPipe (Hand gesture detection)  
- 🖱 PyAutoGUI (Simulate mouse clicks)  

---

## 🛠 How It Works

1. The webcam captures live hand gestures
2. MediaPipe detects hand landmarks in real-time
3. The number of fingers detected determines the gesture:
   - **Open hand (4+ fingers)** = Press and hold GAS button
   - **Closed fist (0–1 fingers)** = Press and hold BRAKE button
4. PyAutoGUI simulates mouseDown and mouseUp at the GAS or BRAKE button positions inside the game

---

## 🚀 How to Run

1. Install required packages:
    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

2. Run the script:
    ```bash
    python gesture_drive.py
    ```

3. Make sure:
   - The game is running in **windowed mode**
   - You start a race with GAS/BRAKE visible
   - You **click once inside the game window** after starting it
   - Webcam is free (not used by other apps)

4. Show your hand to control the car!

---

## 📍 Customize

- Update GAS and BRAKE coordinates in the code:
    ```python
    gas_button_pos = (1721, 649)
    brake_button_pos = (1266, 626)
    ```
    > You can get these positions using:
    ```python
    import pyautogui, time
    time.sleep(5)
    print(pyautogui.position())
    ```

---

## 📸 Screenshots

> *(You can add images later showing your hand + game)*

---

## ✨ Features

- Real-time gesture control
- No external devices required
- Simple and effective control scheme
- Can be adapted for any mouse-based game

---

## 📚 Future Enhancements

- Dual-hand control: left = brake, right = gas
- Turbo with two-hand open
- GUI for easier setup
- Voice + gesture combo

---

## 🙋‍♂️ Author

**Yash Awale**  
Intern @ Rooman Technologies (AI – Data Quality Analyst)

---

## 📜 License

Open-source under MIT License – use, modify, share with credit.

