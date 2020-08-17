## Car Security Using Face Recognition

We are using face recognition using Open CV to implement a new method of security for automobiles on a Raspberry Pi

---

### Final year project
#### Team Members:
- Aditya M Pol
- Amit Anand
- Amith Gowda
- Mohammed Shoaib Baig

---

### Hardware and Components
- Raspberry Pi 3 Model B
- Pi Camera (Or any other webcam)
- Micro SD Card (Min 8GB with Raspberry Pi OS)
- 5v micro-USB power supply

Optional Components to simulate the Automobile functions like door unlock and ignition on:
- Electric Solenoid Lock
- DC Motors
- Motor Driver Circuit (H-Bridge)
- Single Channel Relay
- 12v Power Supply with a break out board

### Block Diagram and Pin Connections

 ![Block Diagram](/assets/block-diagram.png)

 ![Circuit Diagram](/assets/circuit-diagram.png)

 ---

 ### How To Run

 - For the initial setup, create a user and a dataset by running the **[face-datasets.py](facedatasets.py)** program. This Captures a series of images and converts to grayscale. Then it uses the HAAR Cascade filter to return the coordinates of the position of the face in the frame.
 - Run the **[training.py](training.py)** program which applies the LBPH Algorithm to generate the Histogram data of the image as a **[trainer.yml](trainer/trainer.yml)** file and also assigns a user ID to that particular face. (Note: Each face should only have one unique user ID)
 - Run the **[face_recognition.py](face_recognition.py)**  program which takes in test images from a live feed of the camera. If a face is detected using the same HAAR Cascade filter, it again generates histogram data for the test image using LBPH Algorithm. The test data and the trained data are used to calculate the 'confidence' value using Euclidean distance which lets us figure out if both the images are a match. Refer sources for more information.

 ---

 ### Sources

 - <https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html>
 - <https://docs.opencv.org/master/dc/d88/tutorial_traincascade.html>
 - <http://www.scholarpedia.org/article/Local_Binary_Patterns>
 - <https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html#local-binary-patterns-histograms>
 - <https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_api.html#createlbphfacerecognizer>