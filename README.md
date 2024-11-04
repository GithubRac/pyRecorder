# Simple Screen Recorder

A lightweight, easy-to-use screen recording application built with Python. This application allows users to record their screen and save the recording as a video file.

## Features

- Simple GUI interface
- One-click recording start/stop
- Automatic file naming with timestamps
- Records full screen at 20 FPS
- Saves recordings in AVI format

## Prerequisites

Before running the application, make sure you have installed Python 3.6 or higher on your system. You can check your Python version by running:

python --version

## Installation

1. Clone this repository or download the files
2. Open a terminal/command prompt in the project directory
3. Install the required dependencies:

pip install -r requirements.txt


## Usage

1. Start the application:

2. A window will appear with two buttons:
   - Green "Start Recording" button - Click to begin recording
   - Red "Stop Recording" button - Click to end recording

3. When you stop recording, the video file will be automatically saved in the current directory with a name format: `recording_YYYYMMDD_HHMMSS.avi`


## Dependencies

- opencv-python (>= 4.5.0) - For video processing
- Pillow (>= 9.0.0) - For screen capture
- numpy (>= 1.20.0) - For array operations

## Troubleshooting

Common issues and solutions:

1. **OpenCV Installation Issues**

   pip uninstall opencv-python
   pip install opencv-python --upgrade

2. **Screen Capture Not Working**
   - Ensure you have appropriate screen recording permissions enabled in your system settings
   - Try running the application with administrator privileges

3. **High CPU Usage**
   - The application is set to record at 20 FPS. If you experience performance issues, you can modify the FPS in the code

## Limitations

- Currently only supports full screen recording
- No audio recording capability
- Recordings are saved in AVI format only
- No pause/resume functionality

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is released under the MIT License. Feel free to use, modify, and distribute it as you see fit.


