# AI Rock Paper Scissors ✋🪨📄✂️ (Hand Gesture Game)

A real-time Rock–Paper–Scissors game that uses your webcam to detect hand gestures and play against an AI opponent.  
Built using **Python**, **OpenCV**, and **MediaPipe/cvzone hand tracking**.

## Features
- Real-time hand gesture recognition (Rock / Paper / Scissors)
- AI opponent (random choice)
- Score tracking (Player vs AI)
- Round timer (auto delay between rounds)
- Simple on-screen UI

## Tech Stack
- Python
- OpenCV
- MediaPipe (or cvzone HandTrackingModule)
- NumPy

## Project Structure
Rock_Paper_Scissor/
├─ rock_paper_scissors.py
├─ README.md
├─ .gitignore

## Setup (Windows)
> Recommended: use a virtual environment.

### 1) Create & activate venv
```powershell
py -3.11 -m venv rps_env
.\rps_env\Scripts\Activate.ps1
2) Install dependencies
If you’re using cvzone:
pip install opencv-python numpy cvzone mediapipe
(If MediaPipe causes issues on your machine, install a compatible version like:)

pip install mediapipe==0.10.14
python rock_paper_scissors.py

How to Play
Rock: closed fist ✊

Paper: open palm ✋

Scissors: index + middle fingers ✌️

Press Q to quit.

Demo Screenshot

<img width="1920" height="1080" alt="Screenshot 2025-12-18 132250" src="https://github.com/user-attachments/assets/322913c2-45ad-4f6c-bb5e-d9217ad517fc" />


Author
Pushpa Samunuru
