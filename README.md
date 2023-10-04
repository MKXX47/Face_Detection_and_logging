# Face_Detection_and_logging

This Python script captures video from the default camera (usually the webcam) and performs real-time face detection using the OpenCV library. It logs the timestamp and the number of faces detected to a CSV file.

## Prerequisites

- Python installed on your system.
- OpenCV (`cv2`) library installed.
- A CSV file name should be provided as a command-line argument when running the script.

## Script Overview

The script performs the following actions:

1. Initializes the camera capture and loads the pre-trained face detection model from 'haarcascade_frontalface_default.xml'.

2. Captures video frames from the camera.

3. Converts each frame to grayscale for face detection.

4. Detects faces in the grayscale frame using the Haar Cascade Classifier.

5. Keeps track of detected faces and logs the timestamp and the number of faces detected to the specified CSV file.

6. Displays the video feed with rectangles drawn around detected faces.

7. The script runs for a maximum of 240 seconds (4 minutes) or until the user presses 'q' to exit.

## Usage

1. Run the script using Python and provide the CSV file name as a command-line argument:
python script_name.py output.csv

2. The script will start capturing video and perform real-time face detection.

3. Detected faces will be highlighted with green rectangles, and information about the detection will be logged to the specified CSV file.

4. To exit the script, press 'q' in the video feed window.

## Note

- This code is a basic example of real-time face detection using OpenCV. You can customize it further by changing the Haar Cascade Classifier, adjusting detection parameters, or incorporating additional features.

- Ensure you have OpenCV installed (`pip install opencv-python`).

- The CSV file will contain timestamped records of detected faces, which can be useful for various applications, such as attendance tracking or security monitoring.

- For production use, consider using more advanced face recognition techniques for improved accuracy and security.

- Make sure to customize and expand this code as needed for your specific use case.
