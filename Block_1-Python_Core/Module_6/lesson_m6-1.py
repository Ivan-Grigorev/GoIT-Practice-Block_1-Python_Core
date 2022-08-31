from pathlib import Path


message = "Hello world!"

print(message.encode())
print(message.encode("utf_16"))
print(message.encode("cp1251"))

print(b"\xec\xe8\xf0!".decode("cp1251"))

folder = Path('Test')

with open(folder / "utf-8.txt", "wb") as f:
    f.write(message.encode("utf-8"))
with open(folder / "utf-16.txt", "wb") as f:
    f.write(message.encode("utf_16"))
with open(folder / "cp1251.txt", "wb") as f:
    f.write(message.encode("cp1251"))

with open(folder / "utf-8.txt", "rb") as f:
    print(f.read().decode("utf-8"))
with open(folder / "utf-16.txt", "rb") as f:
    print(f.read().decode("utf-16"))
with open(folder / "cp1251.txt", "rb") as f:
    print(f.read().decode("cp1251"))

#################

from pathlib import Path
import os


cur_path = Path()
print(cur_path.cwd())

folder = cur_path / "bin" / "utils" / "paint.example.jpg"
# print(folder)
# print(cur_path.joinpath("bin", "utils", "paint.example.jpg"))
# print(folder.parts)
# print(folder.name)
# print(folder.parent)
# print(folder.suffix)
# print(folder.suffixes)

# print(os.name)  # posix nt

# list_dir = Path(".")
#
# for el in list_dir.iterdir():
#     if el.is_dir():
#         print(f"{el.name} - it's directory")
#     if el.is_file():
#         print(f"{el.name} - it's file")

# not_exist = Path('head.py')
# print(not_exist.exists())

# *.py  **/*.py **/**/*.py

# for el in list_dir.glob("*.py"):
#     print(el)

try:
    tmp = Path("test.txt")
    tmp.unlink()
except FileNotFoundError:
    pass

new_dir = Path("Test")
if not new_dir.exists():
    new_dir.mkdir()

new_dir = Path("Test/temp/asd/baz")
new_dir.mkdir(parents=True, exist_ok=True)

##################

import sys


NUM_LINES = 10

if len(sys.argv) != 2:
    print('Filename not passed to read')
    quit()

try:
    inf = open(sys.argv[1], "r", encoding="utf-8")
    try:
        line = inf.readline()
        count = 0
        while count < NUM_LINES and line != "":
            line = line.rstrip()
            count += 1
            print(line)
            line = inf.readline()
    except OSError:
        print('File read error')
    finally:
        inf.close()
except OSError:
    print('File access error')

#################

from pathlib import Path


path_text = Path('Test/my_txt_file.txt')
path_text.write_text('Test dfhfdhf\nSdff')
path_text.write_text('AAAaaaa')
print(path_text.read_text())

path_bytes = Path('Test/my_bin_file.bin')
path_bytes.write_bytes(b'Test dfhfdhf\nSdff')
path_bytes.write_bytes(b'AAAaaaa')
print(path_bytes.read_bytes())

###################

from pathlib import Path


folder = Path('Temp')

try:
    with open(folder / "temp.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.rstrip())
except OSError:
    print('File access error')

try:
    file = open(folder / "temp.txt", "r", encoding="utf-8")
    try:
        while True:
            line = file.readline()
            print(line)
            if not line:
                break
            print(line.rstrip())
    except OSError:
        print("Error IO")
    finally:
        file.close()
except OSError:
    print('File access error')

###################

import sys


NUM_LINES = 10

if len(sys.argv) != 2:
    print('Filename not passed to read')
    quit()

try:
    with open(sys.argv[1], "r", encoding="utf-8") as inf:
        lines = []
        for line in inf:
            lines.append(line)
            if len(lines) > NUM_LINES:
                lines.pop(0)
        for line in lines:
            print(line, end="")
except OSError:
    print('File access error')

#################

from pathlib import Path


folder = Path('Temp')
list_data = ["Natalia", "Inna", "Andriy", "Ivan"]

try:
    with open(folder / "data.txt", "w", encoding="utf-8") as f:
        for line in list_data:
            f.write(line + "\n")
except OSError:
    print('File access error')

try:
    with open(folder / "data-all.txt", "a", encoding="utf-8") as f:
        f.writelines(["Natalia\n", "Inna\n", "Andriy\n", "Ivan\n"])
except OSError:
    print('File access error')
