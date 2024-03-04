import sys


def my_tail(files):
    if not files:
        # не получили файлы
        lines = sys.stdin.readlines()
        for line in lines[max(0, len(lines) - 17):]:
            print(line, end="")
    else:
        # получили файлы
        for i, file in enumerate(files):
            print(f"==> {file} <==")
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines[max(0, len(lines) - 10):]:
                    print(line, end="")
            print("")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        my_tail(sys.argv[1:])
    else:
        my_tail(None)
