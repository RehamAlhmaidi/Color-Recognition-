# Color-Recognition-
This project demonstrates real-time color recognition using OpenCV.



## Overview
This project demonstrates real-time color recognition using OpenCV. It includes two implementations:
1. **HSV Color Selector** - Allows users to explore HSV color values using trackbars.
2. **Real-Time Color Detection** - Captures video from a webcam and detects the dominant color at the center of the frame.


## Features
- Real-time HSV color selection with adjustable sliders.
- Live webcam feed for detecting colors at the center of the frame.
- Recognizes basic colors: **Red, Orange, Yellow, Green, Blue, Purple, Pink, Gray, White, and Black**.
- Displays detected color name with corresponding background color.
- A small circle at the center of the frame determines the detected color.



## Installation
To run this project, ensure you have Python and OpenCV installed. You can install the required dependencies using:
```sh
pip install opencv-python numpy
```


## Usage
### 1. HSV Color Selector
This script allows you to explore different colors using HSV values.
Run the following command:
```sh
python hsv_color_selector.py
```



**Controls:**
- Adjust **Hue (H)**, **Saturation (S)**, and **Value (V)** using trackbars.
- The window updates in real-time to show the selected color.
- Press `Esc` to exit.



### 2. Real-Time Color Detection
This script detects the color at the center of the webcam feed.
Run the following command:
```sh
python color_recognition.py
```


**How it works:**
- The script captures video from the webcam.
- It converts the frame to HSV and extracts the color at the center.
- The detected color is displayed at the top-left corner.
- Press `Esc` to exit.



## Example Outputs
### HSV Color Selector

![Screenshot 2025-02-04 215139](https://github.com/user-attachments/assets/511acb3c-7ed2-47bb-9a2f-94737814c786)





### Real-Time Color Detection

![Screenshot 2025-02-04 225818](https://github.com/user-attachments/assets/80fe5a13-a4a8-4cb7-8449-a86cba7cb09f)



## Source Code

- [color_recognition.py](c_detection.py) - Detects colors in real-time.
- [hsv_color_selector.py](HSV.py) - Interactive HSV color selection.



## Future Improvements
- Extend color detection to include more nuanced shades.
- Improve accuracy by using a region-based color detection instead of a single pixel.
- Implement a GUI-based application for better user experience.



## Author
[Reham Alhmaidi] - Developed as part of an OpenCV-based project.


