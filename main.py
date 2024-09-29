# Created by Patrick Jennewein
# October 9, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse

def main():
    try:
        # parse the command line
        args = parse()

        image = cv2.imread(args['image'])

        if image is None:
            print(f"Invalid image file.")

        cv2.imshow("rendering", image)
        cv2.waitKey()

        # Close any open display windows once user quits
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0

if __name__ == '__main__':
    main()
