import pandas as pd

# Укажите путь к исходному файлу
input_file = 'vehicles.csv'
output_file = 'vehicles.csv'

# Загружаем первые 106720 строк
df = pd.read_csv(input_file, nrows=106720)

# Сохраняем результат в новый CSV файл
df.to_csv(output_file, index=False)

print(f"Файл обрезан до 106720 строк и сохранен как {output_file}")