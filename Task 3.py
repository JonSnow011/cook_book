import os

# Функция для чтения содержимого файла и получения количества строк
def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.readlines()
    return content, len(content)

# Получаем список файлов в текущей директории
files = [file for file in os.listdir() if os.path.isfile(file)]

# Создаем список для хранения содержимого и количества строк в каждом файле
file_contents = []

# Читаем содержимое каждого файла и добавляем его в список file_contents
for file in files:
    content, num_lines = read_file(file)
    file_contents.append((file, num_lines, content))

# Сортируем список file_contents по количеству строк в каждом файле
file_contents.sort(key=lambda x: x[1])

# Записываем отсортированное содержимое файлов в новый файл
output_filename = "output.txt"
with open(output_filename, 'w', encoding='utf-8') as output_file:
    for file_info in file_contents:
        output_file.write(f"{file_info[0]}\n{file_info[1]}\n")
        output_file.writelines(file_info[2])
        output_file.write("\n")

print("Файл успешно создан:", output_filename)