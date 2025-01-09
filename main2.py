import os
import pandas as pd

file_path = "vehicles.csv"
file_size = os.path.getsize(file_path)
print(f"Объем файла на диске: {file_size / (1024 * 1024):.2f} MB")

df = pd.read_csv(file_path)

# Общий объем памяти, занимаемый DataFrame
memory_usage = df.memory_usage(deep=True).sum()
print(f"Объем памяти, занимаемый набором данных: {memory_usage / (1024 * 1024):.2f} MB")

# Объем памяти для каждой колонки
column_memory = df.memory_usage(deep=True)

# Доля от общего объема памяти
column_memory_percentage = (column_memory / memory_usage) * 100

# Вывод результатов
print("Объем памяти и доля от общего объема для каждой колонки:")
for column in df.columns:
    print(f"{column}: {column_memory[column] / (1024):.2f} KB, {column_memory_percentage[column]:.2f}% - Тип данных: {df[column].dtype}")
