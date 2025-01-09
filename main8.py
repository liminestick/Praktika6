import pandas as pd

# Задать имена колонок, которые будем использовать
columns_to_use = ['id', 'price', 'year', 'manufacturer', 'model', 'condition',
                  'cylinders', 'fuel', 'odometer', 'transmission']

# Задать типы для каждой из колонок
dtype_mapping = {
    'id': 'int64',
    'price': 'int64',
    'year': 'float64',
    'manufacturer': 'object',
    'model': 'object',
    'condition': 'object',
    'cylinders': 'object',
    'fuel': 'object',
    'odometer': 'float64',
    'transmission': 'object'
}

# Путь к исходному файлу
input_file = 'vehicles.csv'

# Указать путь для сохранения очищенного поднабора данных
output_file = 'vehicles_subset_cleaned.csv'

# Чтение данных чанками с преобразованием типов и сохранение поднабора
chunksize = 10000  # Размер чанка

# Инициализация пустого списка для хранения данных
chunk_list = []

# Чтение данных по чанкам
for chunk in pd.read_csv(input_file, usecols=columns_to_use, dtype=dtype_mapping, chunksize=chunksize):
    # Очистка данных, например, удаление строк с пропущенными значениями
    chunk_cleaned = chunk.dropna()

    # Добавление обработанного чанка в список
    chunk_list.append(chunk_cleaned)

# Объединение всех чанков в один DataFrame
full_cleaned_data = pd.concat(chunk_list)

# Сохранение очищенного поднабора в новый файл
full_cleaned_data.to_csv(output_file, index=False)

print("Поднабор данных очищен и сохранен в", output_file)
