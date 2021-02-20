import argparse
import sys

from entities.method import OrganiseMethod


def run(grab):
    OrganiseMethod(grab.d, grab.o)
    return 'Finish'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', type=str, default=None,
                        help="Give the directory address")

    parser.add_argument('-o', type=str, default=None,
                        help="Give the organising method")

    args = parser.parse_args()
    sys.stdout.write(run(args))
