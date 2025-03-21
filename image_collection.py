import os
import cv2 as cv

DATA_DIR = "./data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_gest = 3
size = 100

cap = cv.VideoCapture(0)

for j in range(number_of_gest):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print(f"Collecting data for class{j}")    

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Video capture error')
            break
        cv.putText(frame, 'Ready ? Press Q ;)', (100, 50), cv.FONT_HERSHEY_COMPLEX, 
                   1.3, (0, 0, 255), 4, cv.LINE_AA )
        cv.imshow('Collection frame', frame)

        if cv.waitKey(25) == ord('q'):
            break

    counter = 0

    while counter < size:
        ret, frame = cap.read()
        if not ret:
            print('Video Capture Error')
            break
        cv.imshow('frame', frame)
        cv.waitKey(25)
        cv.imwrite(os.path.join(DATA_DIR, str(j), f"{counter}.jpg"), frame)

        counter += 1

cap.release()
cv.destroyAllWindows()