Sign-Language-To-Text-and-Speech-Conversion

ABSTRACT:

Sign language is one of the oldest and most natural forms of language for communication. This project presents a real-time method using neural networks for finger spelling-based American sign language. Automatic human gesture recognition from camera images is an interesting topic for developing vision. We propose a convolution neural network (CNN) method to recognize hand gestures of human actions from an image captured by a camera. The purpose is to recognize hand gestures of human task activities from a camera image. The position of the hand and orientation are applied to obtain the training and testing data for the CNN. The hand is first passed through a filter and then through a classifier which predicts the class of the hand gestures. Then the calibrated images are used to train CNN.

Introduction:

American sign language is a predominant sign language. Since the only disability deaf and mute people have is communication-related and they cannot use spoken languages, the only way for them to communicate is through sign language. Communication is the process of exchanging thoughts and messages in various ways such as speech, signals, behavior, and visuals. Deaf and mute people make use of their hands to express different gestures to communicate their ideas with other people. Gestures are the nonverbally exchanged messages and these gestures are understood with vision. This nonverbal communication of deaf and mute people is called sign language.

This project focuses on producing a model that can recognize finger-spelling-based hand gestures to form a complete word by combining each gesture.

Requirements:

More than 70 million deaf people around the world use sign languages to communicate. Sign language allows them to learn, work, access services, and be included in their communities. It is hard to make everybody learn the use of sign language to ensure that people with disabilities can enjoy their rights on an equal basis with others.

The aim is to develop a user-friendly human-computer interface (HCI) where the computer understands the American sign language. This project will help deaf and mute people by making their lives easier.

Objective:

To create a computer software and train a model using CNN that takes an image of a hand gesture of American Sign Language, displays the output of the particular sign language in text format, and converts it into audio format.

Scope:

This system will be beneficial for both deaf/mute people and those who do not understand sign language. The system will identify the gestures and provide output in the form of text as well as speech format.

Modules:

Data Acquisition:

The different approaches to acquiring data about the hand gesture include electromechanical devices that provide exact hand configuration and position. Different glove-based approaches can be used to extract information, but they are expensive and not user-friendly.

In vision-based methods, the computer webcam is the input device for observing the information of hands and/or fingers. Vision-based methods require only a camera, thus realizing a natural interaction between humans and computers without the use of extra devices, thereby reducing costs.

The main challenge of vision-based hand detection is coping with the large variability of the human hand’s appearance due to a huge number of hand movements, different skin-color possibilities, as well as variations in viewpoints, scales, and speed of the camera capturing the scene.

Data Pre-processing and Feature Extraction:

For hand detection, we detect the hand from an image acquired by a webcam. To detect a hand, we used the MediaPipe library for image processing. After finding the hand in the image, we extract the region of interest (ROI), crop the image, and convert it to a grayscale image using the OpenCV library. We then apply a Gaussian blur filter.

Next, we convert the grayscale image into a binary image using threshold and adaptive threshold methods. We have collected images of different signs of different angles for sign letters A to Z.

To improve recognition accuracy, we use a method that detects the hand using MediaPipe, extracts the hand landmarks, and draws them on a plain white background using OpenCV. This method eliminates background and lighting condition issues.

We have collected 180 skeleton images of Alphabets from A to Z.

Gesture Classification:

Convolutional Neural Network (CNN)

CNN is a class of neural networks that are highly useful in solving computer vision problems. They are inspired by the actual perception of vision in the human brain. CNNs make use of a filter/kernel to scan through the entire pixel values of the image and make computations by setting appropriate weights to enable the detection of specific features. CNN is equipped with layers such as the convolution layer, max pooling layer, flatten layer, dense layer, dropout layer, and a fully connected neural network layer. These layers together make a very powerful tool that can identify features in an image.

Unlike regular neural networks, CNN neurons are arranged in three dimensions: width, height, and depth. The neurons in a layer are only connected to a small region of the layer before it instead of all neurons in a fully connected manner.

The final output layer has dimensions based on the number of classes. By the end of the CNN architecture, the full image is reduced into a single vector of class scores.

Pooling Layer:

Pooling layers are used to decrease the size of the activation matrix and reduce the number of learnable parameters. There are two types of pooling:

Max Pooling: Takes a window of a specific size (e.g., 2x2) and selects the maximum value within that window.

Average Pooling: Takes the average of all values in a window.

Fully Connected Layer:

In a fully connected layer, all inputs are connected to neurons, unlike the convolution layer, where neurons are connected only to a local region.

The preprocessed 180 images per alphabet are fed into the Keras CNN model. Initially, we encountered poor accuracy in 26 different classes. To improve accuracy, we divided the 26 different alphabets into 8 classes, grouping similar alphabets together.

Each gesture label is assigned a probability, and the label with the highest probability is considered the predicted label.

Using our method, we achieved 97% accuracy under varying lighting conditions and backgrounds. Under ideal conditions (clear background and good lighting), the accuracy reached 99%.

Text-To-Speech Translation:

The model translates recognized gestures into words. We use the pyttsx3 library to convert the recognized words into speech. The text-to-speech output is a useful feature that simulates real-life dialogue.

Project Requirements:

Hardware Requirement:

Webcam

Software Requirement:

Operating System: Windows 8 and Above

IDE: VS CODE

Programming Language: Python 3.9

Python Libraries: OpenCV, NumPy, Keras, MediaPipe, TensorFlow

System Diagrams:

System Flowchart

Use-case diagram

Sequence diagram

This project provides an efficient solution for sign language recognition, aiming to bridge the communication gap for the deaf and mute community.
