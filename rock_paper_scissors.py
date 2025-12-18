import cv2
import numpy as np
import random
import time
from cvzone.HandTrackingModule import HandDetector

# ---------------- SETUP ----------------
cap = cv2.VideoCapture(0)

# cvzone hand detector (uses MediaPipe internally but stable API)
detector = HandDetector(detectionCon=0.7, maxHands=1)

# Game variables
choices = ["ROCK", "PAPER", "SCISSORS"]
player_score = 0
ai_score = 0
result_text = ""
ai_choice = ""

# Timer variables
round_delay = 3        # seconds between rounds
show_timer = False
timer_start = 0

# ---------------- HELPER FUNCTIONS ----------------
def get_player_choice(fingers_4):
    """
    fingers_4 = [index, middle, ring, pinky] as booleans
    """
    if fingers_4 == [False, False, False, False]:
        return "ROCK"
    elif fingers_4 == [True, True, True, True]:
        return "PAPER"
    elif fingers_4 == [True, True, False, False]:
        return "SCISSORS"
    else:
        return None


def get_winner(player, ai):
    if player == ai:
        return "DRAW"
    if (player == "ROCK" and ai == "SCISSORS") or \
       (player == "SCISSORS" and ai == "PAPER") or \
       (player == "PAPER" and ai == "ROCK"):
        return "PLAYER"
    return "AI"


# ---------------- MAIN LOOP ----------------
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    player_choice = None

    # Detect hands
    hands, frame = detector.findHands(frame, draw=True)

    if hands:
        hand = hands[0]
        fingers5 = detector.fingersUp(hand)  # [thumb, index, middle, ring, pinky]
        fingers4 = [bool(x) for x in fingers5[1:]]  # ignore thumb -> [index, middle, ring, pinky]

        player_choice = get_player_choice(fingers4)

        if player_choice and not show_timer:
            cv2.putText(frame,
                        f"Your Move: {player_choice}",
                        (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2)

    current_time = time.time()

    # ---------------- TIMER LOGIC ----------------
    if show_timer:
        elapsed = current_time - timer_start
        remaining = round_delay - int(elapsed)

        if remaining <= 0:
            show_timer = False
            result_text = ""
            ai_choice = ""
        else:
            cv2.putText(frame,
                        f"Next round in: {remaining}",
                        (350, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 255),
                        3)

    # ---------------- GAME LOGIC ----------------
    elif player_choice:
        ai_choice = random.choice(choices)
        winner = get_winner(player_choice, ai_choice)

        if winner == "PLAYER":
            player_score += 1
            result_text = "YOU WIN!"
        elif winner == "AI":
            ai_score += 1
            result_text = "AI WINS!"
        else:
            result_text = "DRAW!"

        show_timer = True
        timer_start = current_time

    # ---------------- UI ----------------
    cv2.rectangle(frame, (0, 0), (w, 120), (0, 0, 0), -1)

    cv2.putText(frame,
                f"Player: {player_score}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2)

    cv2.putText(frame,
                f"AI: {ai_score}",
                (200, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2)

    if ai_choice:
        cv2.putText(frame,
                    f"AI Move: {ai_choice}",
                    (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2)

    if result_text:
        cv2.putText(frame,
                    result_text,
                    (350, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3)

    cv2.putText(frame,
                "Show hand | Q to quit",
                (10, h - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)

    cv2.imshow("AI Rock Paper Scissors", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
