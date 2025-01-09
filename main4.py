import pandas as pd

# Укажите путь к вашему CSV файлу
file_path = 'vehicles.csv'

# Загружаем данные
df = pd.read_csv(file_path)

# Функция для преобразования колонок 'object' в 'category' на основе количества уникальных значений
def convert_objects_to_category(df):
    for column in df.select_dtypes(include=['object']).columns:
        unique_count = df[column].nunique()
        total_count = len(df[column])
        # Если уникальных значений меньше 50% от общего числа строк
        if unique_count / total_count < 0.5:
            df[column] = df[column].astype('category')
    return df

# Преобразуем 'object' колонки в 'category'
df = convert_objects_to_category(df)

# Сохраняем результат в новый CSV файл
output_file = 'vehicles_10000.csv'
df.to_csv(output_file, index=False)

print(f"Преобразование выполнено. Результат сохранен в {output_file}")
