# Image Sampling and Processing

This project performs image processing tasks such as downsampling and upsampling, with support for different downsampling techniques and intensity adjustments. The user can specify various parameters via command-line arguments to control the sampling behavior.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Arguments](#arguments)

## Installation

### Prerequisites
To run the project, you'll need the following:

- Python 3.9 or higher

Required libraries:
- `opencv-python~=4.10.0.84`
- `numpy~=2.1.0`

Additionally, the `argparse` library is used to handle command-line arguments, which is part of the Python standard library.

### Installing

To install and set up the project:
```bash
git clone https://github.com/patrick-jennewein/CS5420-Project-3.git
cd CS5420-Project-3
pip install -r requirements.txt
```

## Usage
The program can be run using the following command:

```bash
Copy code
python main.py [-h] -i IMAGE -d DEPTH -s OPERATION -o OUTPUT [-i INTENSITY]
```
### Arguments
Positional Arguments:
* IMAGE (required): Path to the input image file. 

Optional Arguments:
* -h : Show help message and exit.
* -d DEPTH : Downsampling depth (integer value, higher depth means more downsampling).
* -s OPERATION : Specify the operation to perform. Options:
  * 1 for downsampling by removal followed by upsampling by copying.
  * 2 for downsampling by averaging followed by upsampling by interpolation.
* -i INTENSITY : Intensity downsampling depth (integer value). Optional, defaults to 1.

### Example Usage:
```bash
Copy code```
python main.py my_image.jpg -d=2 -s=1 -i=3
```
This command will process the input image `my_image.jpg`, downsample it using operation 1 with a depth of 2, then apply intensity downsampling with a depth of 3.

### Project Description
The main script (main.py) allows the user to load an image, downsample it, and optionally perform intensity downsampling. 

Several operations are available for downsampling and upsampling:
* Operation 1 (Downsampling by Removal):
  * Rows and columns are removed to reduce the size.
  * After downsampling, the image is upsampled by copying pixels.
* Operation 2 (Downsampling by Averaging):
  * Averages nearby pixels to reduce the size.
  * After downsampling, the image is upsampled by interpolation.
* Additionally, an intensity downsampling option reduces the bit-depth of the image to simulate a lower quality version.

The script uses OpenCV for image handling and manipulation.

### Files
* `main.py`: The main entry point for the application. Handles command-line arguments and calls the image processing functions.
* `sampling_ops.py`: Contains the functions for performing downsampling (both removal and averaging) and upsampling (copying and interpolation). It also includes the function for intensity downsampling.
* `parse_args.py`: Handles the parsing of command-line arguments.
