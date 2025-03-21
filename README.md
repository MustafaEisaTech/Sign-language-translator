# 🖐️ Sign Language Translator  
A real-time sign language recognition system using **Ensemble Learning**. This project processes hand gestures and translates them into text using a combination of multiple machine learning models for improved accuracy and robustness.

## 📌 Project Overview  
This system processes live video input, detects hand gestures, and translates them into corresponding text. The model leverages **Ensemble Learning**, combining multiple classifiers to improve prediction accuracy.

![Demo](images/project_demo.gif)

---

## 🎯 Features  
✅ **Real-time hand gesture recognition** using OpenCV  
✅ **Robust classification with Ensemble Learning**  
✅ **Supports multiple sign language gestures** (extendable with custom datasets)  
✅ **Web-based Interface (Future Work)**  
✅ **Custom dataset support** for training new gestures  
✅ **Live video feedback** with gesture predictions overlaid on the video stream  
✅ **Model persistence** using `pickle` for easy deployment  

---

## 📂 Folder Structure  
sign-language-translator/
│── data/                    # Folder containing gesture data
│   ├── 0/                   # Images for gesture 0
│   ├── 1/                   # Images for gesture 1
│   └── 2/                   # Images for gesture 2
│── images/                  # Images for documentation
│   └── project_demo.gif     # Demo GIF
│── .gitignore               # Git ignore file
│── data.pickle              # Pickle file for processed data
│── Dataset_creation.py      # Script for creating dataset
│── image_collection.py      # Script for collecting images
│── inference.py             # Script for real-time inference
│── LICENSE                  # License file
│── main.py                  # Main script to run the translator
│── model.p                  # Trained model file
│── README.md                # Project documentation
└── train_model.py           # Script for training the model
---

## 🛠️ Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/sign-language-translator.git
   cd sign-language-translator

---
## 🛠️ Dependencies
Python Version: 3.10

Libraries:

OpenCV: 4.8.0

MediaPipe: 0.10.0

NumPy: 1.23.5

Scikit-learn: 1.2.2

Pickle: Built-in (no version required)