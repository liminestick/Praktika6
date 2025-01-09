import pandas as pd
import json

# Загрузка первых 10,000 строк данных
df = pd.read_csv("vehicles.csv")

# Вычисление объема памяти для каждой колонки
column_memory = df.memory_usage(deep=True)

# Доля от общего объема памяти
total_memory = column_memory.sum()
column_memory_percentage = (column_memory / total_memory) * 100

# Подготовка данных для JSON
column_stats = []
for column in df.columns:
    column_stats.append({
        "column": column,
        "memory_usage_kb": column_memory[column] / 1024,
        "memory_usage_percentage": column_memory_percentage[column],
        "data_type": str(df[column].dtype)
    })

# Сортировка по занимаемому объему памяти
sorted_column_stats = sorted(column_stats, key=lambda x: x["memory_usage_kb"], reverse=True)

# Экспорт данных в JSON файл
output_data = {
    "statistic": "Data without optimization",
    "columns": sorted_column_stats
}

# Запись в JSON файл
with open("column_memory_stats.json", "w") as f:
    json.dump(output_data, f, indent=4)

print("Данные сохранены в файл column_memory_stats.json")
