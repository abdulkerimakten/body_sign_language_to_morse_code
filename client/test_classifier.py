import cv2 as cv 
import mediapipe as mp
import numpy as np
import pickle

# load model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv.VideoCapture(0)

# load mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

labels_dic = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}

while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    if not ret:
        # If the frame is unreadable, show a blank screen
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        cv.putText(frame, "Camera disconnected", (50, 240), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
        cv.imshow('frame', frame)
        if cv.waitKey(25) == ord('q'):
            break
        continue

    H, W, _ = frame.shape
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, # image to draw
                hand_landmarks, # model output
                mp_hands.HAND_CONNECTIONS, # hand connections
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

        # define values for bounding box for the hand
        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10
        
        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        # predict
        model_prediction = model.predict([np.asarray(data_aux)])
        predicted_digit = labels_dic[int(model_prediction[0])]

        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
        cv.putText(frame, predicted_digit, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv.LINE_AA)

    cv.imshow('frame', frame)
    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()