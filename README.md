A Basic Student Attendance application using Face Detection and Face Recognition using Python. Marks the attendance of the students
directly into an excel file which is saved with the name of the faculty taken input. The entries contain Name, Student ID, and current
Timestamp.

videoToImage.py -- This file is used to capture the images of student through a video which can be stopped by pressing "Q".

Tester.py -- This is the main file which Trains the model and also calls the face_detection file detect the faces in the test image.

face_detection.py -- This file detects the faces in the test image.

xlwriter.py -- This file is called by the tester.py to save the entry of students detected into an excel sheet which is named after the                    teacher whose name was taken as input at the starting.

Functionality in Brief :-
          
