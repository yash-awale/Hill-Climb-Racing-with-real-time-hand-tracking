import cv2
import mediapipe as mp
import pyautogui

# ✅ Set your actual button positions
gas_button_pos = (1721, 649)
brake_button_pos = (1266, 626)

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)
current_action = None  # Track: "gas", "brake", or None

# Detect if hand is open
def is_hand_open(hand_landmarks):
    fingers = []
    tip_ids = [4, 8, 12, 16, 20]

    # Thumb
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers
    for i in range(1, 5):
        if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1) >= 4

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_hand_open(hand_landmarks):
                cv2.putText(frame, "🟢 OPEN HAND - GAS ON", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                if current_action != "gas":
                    pyautogui.mouseUp(brake_button_pos)   # release brake
                    pyautogui.mouseDown(gas_button_pos)   # press gas
                    current_action = "gas"
            else:
                cv2.putText(frame, "🔴 FIST - BRAKE ON", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if current_action != "brake":
                    pyautogui.mouseUp(gas_button_pos)     # release gas
                    pyautogui.mouseDown(brake_button_pos) # press brake
                    current_action = "brake"
    else:
        cv2.putText(frame, "⚪ NO HAND DETECTED", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)
        if current_action == "gas":
            pyautogui.mouseUp(gas_button_pos)
        elif current_action == "brake":
            pyautogui.mouseUp(brake_button_pos)
        current_action = None

    cv2.imshow("Gesture Controller - GAS / BRAKE", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
