import os
from os import path

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
files_dir = os.path.join(cur_path, "files")
print(files_dir)
try:
    os.mkdir(files_dir)
except FileExistsError:
    pass

file_path = os.path.join(files_dir, 'file.txt')
with open(file_path, 'a+') as file:
    file.write("123")
    file.seek(0)
    print(file.read())

print(os.path.exists("file.txt"))


print(file_path)
print(path.basename(file_path))
print(path.dirname(file_path))
print(path.splitext("file.txt"))

print(path.abspath(path.join("..", "testdir")))
