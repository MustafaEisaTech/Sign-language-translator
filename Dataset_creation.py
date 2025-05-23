import pickle
import os
import cv2 as cv
import mediapipe as mp
import matplotlib.pyplot as plt

DATA_DIR = "./data"

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True,max_num_hands = 1, min_detection_confidence = 0.3)

data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = [] # to save x, y landmarks cooridinates 
        img = cv.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)
        

            data.append(data_aux)
            labels.append(dir_) # a numerical value, set to a class later

data_dict = {
    "data":data,
    "labels":labels
}
if data_dict["data"] and data_dict["labels"]:  
    with open("data.pickle", "wb") as f:
        pickle.dump(data_dict, f)
    print("Data successfully saved!")
else:
    print("Error: Empty dataset. No data saved.")