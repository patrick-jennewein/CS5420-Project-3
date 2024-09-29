import argparse


def parse() -> dict:
    """parse command-line arguments or use default arguments if none are given."""
    parser = argparse.ArgumentParser()

    # create necessary argument (directory to parse)
    parser.add_argument("image", help="the image file to evaluate")

    # create optional arguments
    parser.add_argument("-s", type=int, default=1,
                        help="the sampling method [default: 1]\n"
                             "1: pixel deletion or replication\n"
                             "2: pixel average or interpolation\n")
    parser.add_argument("-d", type=int, default=1,
                        help="the number of levels for downsampling [default: 1]\n")
    parser.add_argument("-i", type=int, default=1,
                        help="the intensity levels, between 1 and 7 [default: 1]\n")

    # use the parsed arguments
    args = parser.parse_args()

    # validate
    if args.i < 1 or args.i > 7:
        raise ValueError(f"Error: Intensity level (-i) must be between 1 and 7. You provided: {args.i}")

    if args.s < 1 or args.s > 2:
        raise ValueError(f"Error: Sampling method must be between 1 and 2. You provided: {args.s}")

    print(f"Image file: {args.image}")
    print(f"Sampling Method: {args.s}")
    print(f"Levels for downsampling: {args.d}")
    print(f"Intensity levels: {args.i}")

    # convert to dictionary and return
    args_dict = vars(args)
    return args_dict
