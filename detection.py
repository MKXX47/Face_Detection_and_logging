import cv2
import csv
import time
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Please provide the CSV file name as a command line argument.")
    sys.exit()
csv_file_name = sys.argv[1]

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

start_time = time.time()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
detected_faces = list()

with open(csv_file_name, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)

    while (time.time() - start_time) < 240:
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        num_faces_detected = len(faces)
        output = f'{dt_string} There is {num_faces_detected} face detected'

        for (x, y, w, h) in faces:
            if (x, y, w, h) not in detected_faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                detected_faces.append((x, y, w, h))
                print(output)

                writer.writerow([output])

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()
