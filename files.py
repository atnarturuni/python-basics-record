import os
from os import path
from pathlib import Path

print("ФАЙЛ MAIN.py:")
file = open("main.py", "r")
print(file.read())
file.close()

# print("ФАЙЛ VARIABLES.py")
# with open("variables.py", "r") as file:
#     # открытие файла
#     for line in file:
#         print(line.strip())
# # закрытие файла
#
# print('end')

cur_path = os.getcwd()
files_dir = Path(cur_path) / "files"
print(files_dir)
try:
    files_dir.mkdir()
except FileExistsError:
    pass

file_path = files_dir / 'file.txt'
with file_path.open('a+') as file:
    file.write("123")
    file.seek(0)
    print(file.read())

print(Path("file.txt").exists())

print(file_path)
print(path.basename(file_path))
print(path.dirname(file_path))
print(path.splitext("file.txt"))

print(path.abspath(path.join("..", "testdir")))

TEST = os.environ.get(
    "TEST",
    "default value for environment variable"
)
print("test:", TEST)
