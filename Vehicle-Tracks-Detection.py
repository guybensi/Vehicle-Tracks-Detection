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

def detect_tracks(gray_image):
    """Detect potential vehicle tracks in the image using Canny."""
    # Apply edge detection (Canny)
    edges = cv2.Canny(gray_image, 50, 150)

    # Return the edges as the final track mask
    return edges

def save_output(image, output_path):
    """Save the processed image to the specified path."""
    cv2.imwrite(output_path, image)

def main(image_path):
    """Main function to handle the full pipeline."""
    # Preprocess the image
    original_image, gray_image = preprocess_image(image_path)

    # Detect tracks using Canny edge detection
    track_mask = detect_tracks(gray_image)

    # Create an output image directly from the edge detection result
    output_image = cv2.cvtColor(track_mask, cv2.COLOR_GRAY2BGR)

    # Generate output directory based on the input image name
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    output_dir = os.path.join(os.path.dirname(image_path), f"{name}_OUTPUT")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the processed images in the new directory
    output_image_path = os.path.join(output_dir, f"{name}.OUTPUT{ext}")
    edge_image_path = os.path.join(output_dir, f"{name}.edges{ext}")

    # Save outputs
    save_output(output_image, output_image_path)
    save_output(track_mask, edge_image_path)

    print(f"Processed images saved in: {output_dir}")

if __name__ == "__main__":
    # Example usage
    image_path = input("Enter the path to the input image: ").strip()

    main(image_path)
