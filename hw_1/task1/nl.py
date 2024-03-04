import sys


def my_nl(file):
    line_number = 1
    if file:
        file_handle = open(file, 'r')
    else:
        file_handle = sys.stdin

    with file_handle as f:
        for line in f:
            print(f"    {line_number} {line}", end='')
            line_number += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        my_nl(sys.argv[1])
    else:
        my_nl(None)
