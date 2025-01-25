import cv2
import numpy as np
import os

def preprocess_image(image_path):
    """Read and preprocess the image for track detection."""
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray_image

def detect_tracks(gray_image, track_spacing=100, min_track_length=100):
    """Detect potential vehicle tracks in the image."""
    # Apply edge detection (Canny)
    edges = cv2.Canny(gray_image, 50, 150)

    # Apply morphological operations to enhance track-like structures
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    processed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours (potential tracks)
    contours, _ = cv2.findContours(processed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on spacing and length
    track_mask = np.zeros_like(gray_image, dtype=np.uint8)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w >= track_spacing and h >= min_track_length:
            cv2.drawContours(track_mask, [contour], -1, 255, thickness=cv2.FILLED)

    return track_mask

def save_output(image, output_path):
    """Save the processed image to the specified path."""
    cv2.imwrite(output_path, image)

def main(image_path, output_dir, track_spacing=100, min_track_length=100):
    """Main function to handle the full pipeline."""
    # Preprocess the image
    original_image, gray_image = preprocess_image(image_path)

    # Detect tracks
    track_mask = detect_tracks(gray_image, track_spacing, min_track_length)

    # Create a binary output image (tracks = white, everything else = black)
    output_image = np.zeros_like(original_image)
    output_image[track_mask > 0] = [255, 255, 255]

    # Save the output
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"processed_{os.path.basename(image_path)}")
    save_output(output_image, output_path)

    print(f"Output saved at: {output_path}")

# Placeholder function for future motorcycle track detection
def detect_single_track(*args, **kwargs):
    """Future implementation for detecting single motorcycle tracks."""
    pass

if __name__ == "__main__":
    # Example usage
    image_path = input("Enter the path to the input image: ").strip()
    output_dir = input("Enter the directory to save the output: ").strip()

    # Default parameters
    track_spacing = 100  # Distance between tracks in pixels (default 1 meter)
    min_track_length = 100  # Minimum track length in pixels

    main(image_path, output_dir, track_spacing, min_track_length)
