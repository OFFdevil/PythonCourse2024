FROM python:3.9

COPY main.py main.py
COPY array.txt array.txt

RUN apt-get update
RUN apt-get install -y texlive
RUN pip install MyLibrary111111==1.1
RUN python3.9 main.py array.txt
RUN pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=/artifacts artifacts/latex.tex
