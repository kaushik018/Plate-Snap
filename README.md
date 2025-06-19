# Vehicle Number Plate Detector

A real-time vehicle number plate detection system using OpenCV and Haar Cascade classifier.

## Features

- Real-time license plate detection from webcam feed
- Save detected license plates with a single keypress
- Adjustable detection parameters
- Visual feedback for plate detection and saving

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/vehicle-plate-detector.git
cd vehicle-plate-detector
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the detector:
```bash
python src/plate_detector.py
```

2. Controls:
- Press 's' to save a detected license plate
- Press 'q' to quit the application

## Project Structure

```
vehicle-plate-detector/
├── src/              # Source code
├── models/           # Haar cascade model files
├── output/plates/    # Saved license plate images
└── requirements.txt  # Project dependencies
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 