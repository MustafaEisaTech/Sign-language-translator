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
│── data/                    
│   ├── 0/                   
│   ├── 1/                   
│   └── 2/                   
│── images/                  
│   └── project_demo.gif     
│── .gitignore               
│── data.pickle              
│── Dataset_creation.py      
│── image_collection.py      
│── inference.py             
│── LICENSE                  
│── main.py                  
│── model.p                  
│── README.md                
└── train_model.py           
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