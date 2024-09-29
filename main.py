# Created by Patrick Jennewein
# October 9, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from sampling_ops import perform_operation_one

def main():
    try:
        # parse the command line
        args = parse()

        # read and show the image
        image = cv2.imread(args['image'])
        if image is None:
            raise Exception(f"Invalid image file You provided: {args['image']}")
        cv2.imshow("Original Image", image)

        downsampled_image_1 = None
        downsampled_image_2 = None

        # operation 1
        if args['s'] == 1:
            downsample_rate = 2
            downsampled_image = perform_operation_one(image, downsample_rate)

        # operation 2
        elif args['s'] == 2:
            pass

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
