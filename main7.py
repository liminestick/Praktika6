import pandas as pd

# Загрузка данных
df_before = pd.read_csv('vehicles.csv')  # файл до преобразований
df_after = pd.read_csv('vehicles_10000.csv')  # файл после преобразований

# Анализ занимаемой памяти до изменений
memory_before = df_before.memory_usage(deep=True).sum() / (1024 ** 2)  # в мегабайтах
print(f"Объем памяти до изменений: {memory_before:.10f} MB")

# Анализ занимаемой памяти после изменений
memory_after = df_after.memory_usage(deep=True).sum() / (1024 ** 2)  # в мегабайтах
print(f"Объем памяти после изменений: {memory_after:.10f} MB")

# Выводим сравнение
print(f"Разница в объеме памяти: {memory_after - memory_before:.10f} MB")
