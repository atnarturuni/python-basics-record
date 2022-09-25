print("ФАЙЛ MAIN.py:")
file = open("main.py", "w")
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

with open('file.txt', 'a+') as file:
    file.write("123")
    file.seek(0)
    print(file.read())

