import numpy as np
import cv2

def downsample_image(image, downsample_rate):
    """Down-sample the image by removing alternate columns and rows"""
    new_image = image[::downsample_rate, ::downsample_rate]
    cv2.imshow("#1a: Down-sampled Image (half size)", new_image)
    return new_image


def upsample_image(image, downsample_rate):
    """Up-sample the image by copying pixels"""
    # Get the dimensions of the original image
    height, width = image.shape[:2]

    # Create a new empty image of double the size
    upsampled_image = np.zeros((height * downsample_rate,
                                width * downsample_rate,
                                image.shape[2]),
                               dtype=image.dtype)

    # copy pixels
    for row in range(height):
        for col in range(width):
            upsampled_image[downsample_rate * row, downsample_rate * col] = image[row, col]
            upsampled_image[downsample_rate * row + 1, downsample_rate * col] = image[row, col]
            upsampled_image[downsample_rate * row, downsample_rate * col + 1] = image[row, col]
            upsampled_image[downsample_rate * row + 1, downsample_rate * col + 1] = image[row, col]

    cv2.imshow("#1b: Up-sampled Image (original size)", upsampled_image)
    return upsampled_image

def perform_operation_one(image, downsample_rate):
    """combine downsampling and upsampling to return an image that is the same size as original but down-sampled"""
    downsampled_image = downsample_image(image, downsample_rate)
    upsampled_image = upsample_image(downsampled_image, downsample_rate)
    return upsampled_image
