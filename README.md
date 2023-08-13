# GenderGuard
Empowering Secure Spaces with computer vision Gender Detection

# Gender Detection System

This repository contains a gender detection system that utilizes computer vision techniques to detect and classify the gender of individuals appearing in a video stream. The system is built using Python and OpenCV, and it can be used for various applications, including gender-based access control, data collection, and monitoring.

## Table of Contents

- [Introduction](#introduction)
- [Use Cases](#use-cases)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

## Introduction

The gender detection system in this repository utilizes the OpenCV library and HAAR cascade classifiers to identify faces in a video stream and classify their gender as male or female. The system employs HAAR cascade classifiers for face detection and uses OpenCV functionalities to process the video frames. An alarm is triggered specifically when a male face is detected in the video stream.

## Use Cases

The gender detection system can be applied to various scenarios and use cases, including:

1. **Women-Only Spaces**: The system can be deployed in women-only gyms, changing rooms, or restrooms to ensure that only individuals of the appropriate gender are granted access. When a male is detected, an alarm can alert the management.

2. **Gender Data Collection**: The system can be used for data collection purposes, such as gathering statistics on the gender distribution of visitors in specific areas. This data can be valuable for demographic analysis and business decision-making.

3. **Security and Monitoring**: The system can enhance security by monitoring gender-specific areas and triggering alarms if unauthorized individuals enter. It can be utilized in public or private spaces to maintain security protocols.

4. **Event Management**: During events or conferences where gender-specific sessions are held, the system can help ensure that participants enter the correct sessions based on their gender.

5. **Education and Research**: The system can be used in educational or research settings to explore gender-based behaviors, interactions, and preferences within controlled environments.

## Getting Started

To get started with the gender detection system, follow these steps:

### Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- Pygame (for alarm sound)

### Usage

1. Clone this repository to your local machine:

   ```sh
   git clone https://github.com/samaltaa/gender_detection.git
   ```

2. Install the required Python packages:

   ```sh
   pip install opencv-python numpy pygame
   ```

3. Download the Haar Cascade classifier XML file for face detection from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and save it in the repository directory.

4. Download the gender classification model architecture (`deploy_gender.prototxt`) and pre-trained weights (`gender_net.caffemodel`) and place them in the `weights` directory.

5. Customize the system behavior (such as alarm sound, recording duration, etc.) in the code according to your requirements.

6. Run the gender detection system:

   ```sh
   python gender_detection.py
   ```

7. The system will start capturing video from the default camera. When a male face is detected, an alarm will sound.

8. Press 'q' to quit the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify and expand this README to provide more information about your project and its capabilities. Make sure to update the links, paths, and instructions to match your actual project structure and filenames.

Certainly, here's the continuation of the README file:

---

## Acknowledgments

This gender detection system is built upon various open-source libraries and resources. We would like to acknowledge the contributions of the following:

- **OpenCV**: The Open Source Computer Vision Library provides essential tools for computer vision applications, including face detection and image processing.

- **NumPy**: NumPy is the fundamental package for scientific computing with Python. It provides support for handling arrays and matrices, which is crucial for image manipulation.

- **Pygame**: Pygame is a cross-platform set of Python modules designed for writing video games. It's used here for playing the alarm sound.

- **Caffe Model Zoo**: The gender classification model used in this project is based on the Caffe Model Zoo's pre-trained models for gender classification.

## Contributions and Support

Contributions to this project are welcome! If you have any suggestions, bug reports, or improvements, feel free to create an issue or submit a pull request on the GitHub repository.

For questions or support related to this project, you can contact the project maintainer through the GitHub repository.



