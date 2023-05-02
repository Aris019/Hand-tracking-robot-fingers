# Hand-tracking-robot-fingers
The two scripts provided are intended to work together to enable hand gesture recognition and control of servos using an Arduino microcontroller.

The first script, written in Python, uses the cvzone library to detect hand gestures in a video stream from a camera connected to the computer.
It reads the finger state data from the detected hand and sends it to the Arduino board via a serial port. 
This is done by converting the finger state data to a string and formatting it as a serial command using the write() method of the serial module.

The second script, written in the Arduino programming language, runs on the Arduino board and receives the finger state data from the computer via the serial port. 
It parses the received data and uses it to control servos attached to the board. Specifically, the script checks the finger state data for each finger, 
and moves the corresponding servo to either the 180 or 0 position depending on whether the finger is up or down, respectively.

Together, these scripts provide a basic framework for controlling servos using hand gestures detected by a camera connected to a computer. 
By modifying the Python script, it is possible to detect different hand gestures and send different types of data to the Arduino board, 
allowing for a wide range of applications beyond servo control.



This code is using the cvzone library to detect hands in a video stream from the default camera, 
and then sending the finger state data to an Arduino connected to the computer via a serial port.

The HandDetector class is used to detect hands in the video stream. 
The detectionCon parameter specifies the confidence threshold for hand detection, and maxHands specifies the maximum number of hands to detect.

The findHands() method of the HandDetector class is called on each frame of the video stream to detect hands. 
If a hand is detected, various information about the hand is extracted, such as the landmarks of the hand, 
the bounding box around the hand, and the center point of the hand.

The fingersUp() method of the HandDetector class is then called on the hand to determine which fingers are up and which are down. 
The resulting finger state is then converted to a string and formatted as a serial command for the Arduino. 
Finally, the command is sent to the Arduino via the serial port using the write() method of the serial module.

The video stream is displayed using OpenCV's imshow() function and waits for a key press with a 1 millisecond delay using waitKey(1) before capturing the next frame.


C++ code is intended to be uploaded to an Arduino microcontroller that is connected to a computer via a serial port. 
It receives data from the computer in the form of a string, parses the string to extract the finger state data, 
and then uses the extracted data to control servos attached to the Arduino board.

The Servo library is used to control the servos, and five Servo objects are created for the five fingers: thumb, index, middle, ring, and pinky.

The receiveData() function is called repeatedly in the loop() function to check if any data has been received on the serial port. 
If a $ character is received, the counterStart flag is set to true to indicate that the string containing finger state data has started. 
The function then continues to read characters until it has read stringLength number of characters. Once the string has been read, 
it is parsed to extract the finger state data and store it in the valsRec array.

The loop() function then checks the value of each element in the valsRec array, 
and moves the corresponding servo to the 180 position if the value is 1, or to the 0 position if the value is 0. This way,
the servo position is controlled by the finger state data received from the computer via the serial port.

Overall, this code provides a simple example of how to control servos using finger state data from a computer, 
and can be easily modified to control other types of actuators as well.





