import numpy as np
import cv2


def downsample_image_by_removal(image, downsample_rate):
    """down-sample the image by removing columns and rows"""
    new_image = image[::downsample_rate, ::downsample_rate]

    # created a resized window
    window_name = "#1a: Down-sampled Image"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, new_image.shape[1], new_image.shape[0])

    # display the down-sampled image
    cv2.imshow(window_name, new_image)

    return new_image


def upsample_image_by_copying(image, downsample_rate):
    """Up-sample the image by copying pixels, dynamically based on the down-sample rate."""

    # get the dimensions of the original image
    height, width = image.shape[:2]

    # create a new, empty image of the correct up-sampled size
    upsampled_image = np.zeros((height * downsample_rate,
                                width * downsample_rate,
                                image.shape[2]),
                               dtype=image.dtype)

    # copy pixels to a larger area
    """
    Each original pixel will fill an area with the size of the downsample_rate.
    For example, if the downsample_rate is 2, the old 1 x 1 space will now
    fill a 2 x 2 space, decreasing the overall quality of the upsampled image.
    This uses the NumPy slice to achieve this easily.  
    """
    for row in range(height):
        for col in range(width):
            upsampled_image[row * downsample_rate:(row + 1) * downsample_rate,
                            col * downsample_rate:(col + 1) * downsample_rate] = image[row, col]

    cv2.imshow("#1b: Up-sampled Image (original size)", upsampled_image)
    return upsampled_image

def perform_operation_one(image, downsample_rate):
    """combine downsampling and upsampling to return an image that is the same size as original but down-sampled"""
    downsampled_image = downsample_image_by_removal(image, downsample_rate)
    upsampled_image = upsample_image_by_copying(downsampled_image, downsample_rate)
    return upsampled_image
