import pandas as pd

# Укажите путь к вашему CSV файлу
file_path = 'vehicles_10000.csv'

# Загружаем данные
df = pd.read_csv(file_path)

# Функция для преобразования колонок с типом 'int' на более низкий тип
def downcast_int_columns(df):
    for column in df.select_dtypes(include=['int64']).columns:
        # Преобразуем тип в более низкий, если это возможно
        df[column] = pd.to_numeric(df[column], downcast='integer')
    return df

# Понижаем типы колонок 'int'
df = downcast_int_columns(df)

# Сохраняем результат в новый CSV файл
output_file = 'vehicles_10000.csv'
df.to_csv(output_file, index=False)

print(f"Понижающее преобразование типов выполнено. Результат сохранен в {output_file}")
