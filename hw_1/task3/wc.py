import sys


def get_statistic(lines):
    chars, words = 0, 0
    for line in lines:
        chars += len(line)
        words += len(line.split())
    return [len(lines), words, chars]


def my_wc(files):
    if not files:
        lines = sys.stdin.readlines()
        result = get_statistic(lines)
        print(f"{result[0]} {result[1]} {result[2]}")
    else:
        count_chars, count_words, count_lines = 0, 0, 0
        for file in files:
            with open(file, 'r') as f:
                lines = f.readlines()
                result = get_statistic(lines)
                count_lines += result[0]
                count_words += result[1]
                count_chars += result[2]
                print(f"{result[0]} {result[1]} {result[2]} {file}")
        print(f"{count_lines} {count_words} {count_chars} total")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        my_wc(sys.argv[1:])
    else:
        my_wc(None)
