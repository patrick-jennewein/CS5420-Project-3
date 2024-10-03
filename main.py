# Created by Patrick Jennewein
# October 9, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from sampling_ops import perform_operation_one, perform_operation_two, intensity_downsample

def main():
    try:
        # parse the command line
        args = parse()

        # read and show the image
        image = cv2.imread(args['image'])
        if image is None:
            raise Exception(f"Invalid image file You provided: {args['image']}")
        cv2.imshow("Original Image", image)

        new_image = None
        depth = args['d']
        downsample_rate = 2 ** depth

        # operation 1
        if args['s'] == 1:
            new_image = perform_operation_one(image, downsample_rate, depth)

        # operation 2
        elif args['s'] == 2:
            new_image = perform_operation_two(image, downsample_rate, depth)

        if args['i'] > 1:
            new_image = intensity_downsample(new_image, args['i'])



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
