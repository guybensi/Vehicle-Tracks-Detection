# Vehicle Track Detection from Aerial Images

This project is a Python-based tool that detects vehicle tracks from aerial images, specifically in sandy or dune-like terrains. The tool uses OpenCV for image processing to identify clear track marks caused by vehicles, and outputs a binary image where detected tracks are marked in white, and the rest of the image is black.

## Features
- **Input Support**: Accepts RGB images in common formats like JPEG and PNG.
- **Track Detection**: Detects vehicle tracks based on configurable parameters:
  - **Track Spacing**: Distance between wheel tracks (default: 100 pixels).
  - **Minimum Track Length**: Minimum length of continuous tracks to consider as valid (default: 100 pixels).
- **Modular Design**: Functions are divided into logical components for easy debugging and enhancement.
- **Output**: Saves a processed binary image where tracks are highlighted.
- **Extensibility**: Placeholder for future implementation of single-track (motorcycle) detection.

## How It Works
1. **Preprocessing**: Converts the input image to grayscale.
2. **Edge Detection**: Uses the Canny edge detection algorithm to highlight track-like edges.
3. **Morphological Filtering**: Enhances track structures using morphological operations.
4. **Contour Analysis**: Identifies and filters track-like contours based on spacing and length.
5. **Output Image**: Generates and saves a binary image with detected tracks.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/guybensi/Vehicle-Tracks-Detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd vehicle-track-detection
   ```
3. Install the required Python libraries:
   ```bash
   pip install opencv-python opencv-python-headless
   ```

## Usage
Run the script:
```bash
python detect_tracks.py
```
During runtime, provide:
1. **Path to the input image** (e.g., `C:/images/example.jpg`).
2. **Output directory** where the processed image will be saved (e.g., `C:/images/output/`).

### Configurable Parameters
In the script, you can modify:
- **Track Spacing**: Adjust the spacing (in pixels) between tracks.
- **Minimum Track Length**: Set the minimum length (in pixels) of a track to be considered valid.

## Future Enhancements
- **Motorcycle Track Detection**: Add logic to detect single tracks caused by motorcycles.
- **Machine Learning Integration**: Improve detection accuracy using ML models.
- **Batch Processing**: Support processing multiple images in one run.

## Requirements
- Python 3.7 or higher
- OpenCV (install via `pip`)

## Example
Input:  
![Input Image Example](path/to/example-input.jpg)  
Output:  
![Output Image Example](path/to/example-output.jpg)

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.
