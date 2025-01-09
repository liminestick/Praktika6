import pandas as pd

# Укажите путь к вашему CSV файлу
file_path = 'vehicles_10000.csv'

# Загружаем данные
df = pd.read_csv(file_path)

# Функция для понижающего преобразования типов float
def downcast_floats(df):
    for column in df.select_dtypes(include=['float64']).columns:
        # Преобразуем в float32, если это возможно
        df[column] = pd.to_numeric(df[column], downcast='float')
    return df

# Понижаем типы float колонок
df = downcast_floats(df)

# Сохраняем результат в новый CSV файл
output_file = 'vehicles_10000.csv'
df.to_csv(output_file, index=False)

print(f"Понижающее преобразование выполнено. Результат сохранен в {output_file}")
