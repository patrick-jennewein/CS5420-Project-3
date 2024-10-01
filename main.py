# Created by Patrick Jennewein
# October 9, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from sampling_ops import *

def main():
    try:
        # parse the command line
        args = parse()

        # read and show the image
        image = cv2.imread(args['image'])
        if image is None:
            raise Exception(f"Invalid image file You provided: {args['image']}")
        cv2.imshow("Original Image", image)

        downsampled_images = []
        upsampled_images = []
        # downsampled_image_2 = None
        downsample_rate = 2 ** args['d']

        # operation 1
        if args['s'] == 1:
            for i in range(1, args['d'] + 1):
                # downsample and then upsample
                downsampled_image = downsample_image_by_removal(image, 2 ** i)
                downsampled_images.append(downsampled_image)
                upsampled_image = upsample_image_by_copying(downsampled_images[i - 1], 2 ** i)
                upsampled_images.append(upsampled_image)

                # show the images
                cv2.imshow(f"Downsample {image.shape[0] / (2 ** i)} x {image.shape[1] / (2 ** i)}", downsampled_images[i - 1])
                cv2.imshow(f"Upsample {image.shape[0] / (2 ** i)} x {image.shape[1] / (2 ** i)}", upsampled_images[i - 1])

        # operation 2
        # elif args['s'] == 2:
        #     downsampled_image_2 = perform_operation_two(image, downsample_rate)



        # wait for user input
        cv2.waitKey()

        # close any open display windows once user quits
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0

if __name__ == '__main__':
    main()
