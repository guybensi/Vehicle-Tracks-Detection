# Vehicle Track Detection from Aerial Images

This project is a Python-based tool that detects vehicle tracks from aerial images, specifically in sandy or dune-like terrains. The tool uses OpenCV for image processing to identify clear track marks caused by vehicles, and outputs a binary image where detected tracks are marked in white, and the rest of the image is black.

---

## Features
- **Input Support**: Accepts RGB images in common formats like JPEG and PNG.
- **Track Detection**: Detects vehicle tracks based on configurable parameters:
  - **Track Spacing**: Distance between wheel tracks (default: 100 pixels).
  - **Minimum Track Length**: Minimum length of continuous tracks to consider as valid (default: 100 pixels).
- **Modular Design**: Functions are divided into logical components for easy debugging and enhancement.
- **Output**: Saves processed images in a dedicated folder.
- **Extensibility**: Placeholder for future implementation of single-track (motorcycle) detection.

---

## How It Works
1. **Preprocessing**: Converts the input image to grayscale.
2. **Edge Detection**: Uses the Canny edge detection algorithm to highlight track-like edges.
3. **Output Folder**: Saves a binary image highlighting the tracks in a dedicated output folder.

---

## Installation and Setup

### 1. Clone this repository:
```bash
git clone https://github.com/guybensi/Vehicle-Tracks-Detection.git
```

### 2. Navigate to the project directory:
```bash
cd Vehicle-Tracks-Detection
```

### 3. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
```

### 4. Activate the virtual environment:
- **On Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 5. Install required Python libraries:
```bash
pip install opencv-python opencv-python-headless numpy
```

---

## Usage

1. **Run the script**:
   ```bash
   python detect_tracks.py
   ```

2. **Provide the input image path**:  
   For example:
   ```text
   C:\Users\YourUser\Desktop\Images\example.jpg
   ```

3. **Output**:  
   The script will create a folder named `<image_name>_OUTPUT` in the same directory as the input image.  
   Inside this folder, the following files will be saved:
   - **`<image_name>.OUTPUT.jpg`**: The final processed binary image.
   - **`<image_name>.edges.jpg`**: The edge detection result (Canny).

---

## Configurable Parameters
In the script, you can modify:
- **Track Spacing**: Adjust the spacing (in pixels) between tracks.
- **Minimum Track Length**: Set the minimum length (in pixels) of a track to be considered valid.

---

## Future Enhancements
- **Motorcycle Track Detection**: Add logic to detect single tracks caused by motorcycles.
- **Machine Learning Integration**: Improve detection accuracy using ML models.
- **Batch Processing**: Support processing multiple images in one run.

---

## Requirements
- Python 3.7 or higher
- OpenCV (installed via `pip`)
- Numpy (installed via `pip`)

---

## Example

Input:  
![Input Image Example](path/to/example-input.jpg)  
Output:  
![Output Image Example](path/to/example-output.jpg)

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

---
