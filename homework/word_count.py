"""Taller evaluable"""

# pylint: disable=broad-exception-raised

import glob
import os

# Crea la carpeta files/input
if os.path.exists("files/input/"):
    for file in glob.glob("files/input/*"):
        os.remove(file)
else:
    os.makedirs("files/input")


# Crea n copias de cada uno de los archivos en files/raw/
n = 100

for file in glob.glob("files/raw/*"):

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    for i in range(1, n + 1):
        raw_filename_with_extension = os.path.basename(file)
        raw_filename_without_extension = os.path.splitext(raw_filename_with_extension)[
            0
        ]
        new_filename = f"{raw_filename_without_extension}_{i}.txt"
        with open(f"files/input/{new_filename}", "w", encoding="utf-8") as f2:
            f2.write(text)







