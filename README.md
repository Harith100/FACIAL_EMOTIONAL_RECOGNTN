# 😊 Face and Emotion Detection

This project uses **OpenCV** and **DeepFace** to detect faces and analyze emotions in real-time from a webcam feed. The program captures video frames, detects faces, and overlays the detected emotions on the video.

## 🚀 Features

* 🧑‍🤝‍🧑 **Face Detection**: Detects faces using OpenCV's Haar Cascade Classifier.
* 😄 **Emotion Analysis**: Uses DeepFace to analyze emotions from the detected faces.
* 🎥 **Real-Time Video Feed**: Displays live webcam feed with detected emotions.
* 🖥️ **Simple Interface**: Real-time feedback with emotion labels on the video.

## 🛠️ Tech Stack

* **Programming Language**: Python
* **Face Detection**: OpenCV (Haar Cascade Classifier)
* **Emotion Recognition**: DeepFace
* **Computer Vision Library**: OpenCV
* **Webcam Access**: OpenCV VideoCapture

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/face-emotion-detection.git
   cd face-emotion-detection
   ```

2. **Install Dependencies**
   * Install required Python libraries:
   ```bash
   pip install opencv-python deepface
   ```

3. **Run the Application**
   ```bash
   python face2.py
   ```
   * The program will start capturing video from the webcam, and display the dominant emotion detected from the face in real-time.

## 🔧 How it Works

* **Face Detection**: Uses OpenCV's pre-trained Haar Cascade classifier to detect faces in the video frames.
* **Emotion Recognition**: The DeepFace library is used to analyze the emotions on the detected faces, providing a list of emotions and identifying the dominant one.
* **Real-time Display**: The dominant emotion is displayed on the video feed, and faces are highlighted with a rectangle.

## ⚠️ Requirements

* **Python**: Version 3.6 or higher
* **Libraries**:
  * OpenCV
  * DeepFace

## 🙌 Acknowledgements

* DeepFace for emotion analysis.
* OpenCV for face detection and video processing.
