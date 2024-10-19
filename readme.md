# 🎛️WaveVolume

Control your system volume using **hand gestures** with a webcam! This project utilizes **OpenCV**, **MediaPipe**, and **PyCaw** to track hand landmarks and adjust your system's volume based on the distance between your thumb and index finger.


## 🚀 Features

- 🖐️ **Real-Time Hand Tracking**: Tracks hand landmarks using MediaPipe.
- 🔊 **Volume Control**: Adjusts the system volume based on thumb-index distance.
- 🎨 **Customizable**: Easily modify the camera resolution, volume range, and visual feedback.
- ⚡ **Efficient and Lightweight**: Uses efficient algorithms for real-time processing.

## 🛠️ Tech Stack

- ![OpenCV](https://img.shields.io/badge/OpenCV-%23ffffff.svg?style=for-the-badge&logo=opencv&logoColor=black) **OpenCV**: For real-time video capture and image processing.
- ![MediaPipe](https://img.shields.io/badge/MediaPipe-%23ffffff.svg?style=for-the-badge&logo=google&logoColor=black) **MediaPipe**: For hand landmarks detection.
- ![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) **Python**: Programming language used.
- ![PyCaw](https://img.shields.io/badge/PyCaw-%23F7B500.svg?style=for-the-badge&logo=windows&logoColor=black) **PyCaw**: To control system audio via Windows API.

## 📸 How It Works

1. **Hand Detection**: The webcam captures your hand using OpenCV, and MediaPipe detects hand landmarks.
2. **Volume Control**: By calculating the distance between your thumb and index finger, the program adjusts the system's master volume.
3. **Visual Feedback**: Visual cues like lines, circles, and a volume bar give feedback on the current state and hand gestures.

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/namanomar/️WaveVolume.git
cd hand-gesture-volume-control
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the file
```
python main.py
```
