# Color Detection in Images using OpenCV

This project demonstrates how to detect a specific color in an image using the HSV color space with OpenCV. The code focuses on detecting green hues and highlights those regions in the image.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)

## Features

- Convert an image from RGB to HSV color space.
- Apply a mask to highlight specific colors (in this case, green).
- Display the original and processed image side by side for comparison.

## Usage

1. Ensure the image file is located at the specified path.
2. Adjust the lower and upper bounds in the HSV range for detecting other colors if necessary.
3. Run the script to detect colors and display the results:

   ```bash
   python color_detection.py

## License

This project is licensed under the MIT License.
