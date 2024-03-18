import sys
from datetime import datetime

from MyLibrary.my_functions import generate_latex_table, generate_header, generate_image, generate_footer

if __name__ == "__main__":
    name_file_with_table = sys.argv[1]

    with open(name_file_with_table, 'r') as file:
        lines = [line.split() for line in file]

        with open("artifacts/latex.tex", "w") as latex:
            latex.write(generate_header("Latex", "Daniil", str(datetime.now().date())))
            latex.write(generate_latex_table(lines))
            latex.write(generate_image("artifacts/picture.png", 1.5))
            latex.write(generate_footer())

