import cv2 as cv
import pickle
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands  =mp_hands.Hands(static_image_mode = False, min_detection_confidence=0.3, max_num_hands=1)

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']


cap = cv.VideoCapture(0)

labels_dict = {0: 'I Love You', 1: 'Thank You', 2: 'Hello'}
while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()

    H, W, _ = frame.shape
    if not ret:
        print('Video Capture Error')
        break

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmark, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x)
                data_aux.append(y)
                x_.append(x)
                y_.append(y)


        # min and max pixel valeus for the fram
        x1 = int(min(x_) * W)
        x2= int(max(x_) * W)
        y1 = int(min(y_) * H)
        y2 = int(max(y_) * H)

        
        prediction = model.predict([np.asarray(data_aux)])
        predicted_character = labels_dict[int(prediction[0])]
        #print(predicted_character) debugging
        
        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv.putText(frame, predicted_character, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                    cv.LINE_AA)
    cv.imshow('Processing Environment', frame)
        
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
     

cap.release()
cv.destroyAllWindows()
