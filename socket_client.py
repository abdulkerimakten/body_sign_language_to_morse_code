import cv2 as cv
import mediapipe as mp
import numpy as np
import pickle
import socket

# Load the model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# Load Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Labels
labels_dic = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}

# Socket settings
HOST = '192.168.126.44'  # Enter the Raspberry Pi's IP address here
PORT = 65432
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Start the camera
cap = cv.VideoCapture(0)

try:
    while True:
        data_aux = []
        ret, frame = cap.read()

        if not ret:
            print("Camera could not be read!")
            break

        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)

            model_prediction = model.predict([np.asarray(data_aux)])
            digit = int(model_prediction[0])

            # Get the label and send it
            label = labels_dic[digit]  # Retrieve the corresponding label
            sock.sendall(label.encode())  # Send the label

        if cv.waitKey(25) == ord('q'):
            break

finally:
    cap.release()
    sock.close()
    cv.destroyAllWindows()

