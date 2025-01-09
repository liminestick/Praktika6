import sqlite3
import pandas as pd

# Загружаем данные из CSV файла
csv_file_path = 'vehicles.csv'  # Укажите путь к вашему файлу
df = pd.read_csv(csv_file_path, nrows=10000)

# Заменяем NaN на None
df = df.where(pd.notnull(df), None)

# Подключаемся к базе данных SQLite (или создаем новую, если ее нет)
conn = sqlite3.connect('cars.db')  # cars.db — это файл базы данных, который будет создан
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY,
    url TEXT,
    region TEXT,
    region_url TEXT,
    price INTEGER,
    year INTEGER,
    manufacturer TEXT,
    model TEXT,
    condition TEXT,
    cylinders TEXT,
    fuel TEXT,
    odometer TEXT,
    title_status TEXT,
    transmission TEXT,
    VIN TEXT,
    drive TEXT,
    size TEXT,
    type TEXT,
    paint_color TEXT,
    image_url TEXT,
    description TEXT,
    county TEXT,
    state TEXT,
    lat TEXT,
    long TEXT,
    posting_date TEXT
)
''')

# Записываем данные в таблицу
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO cars (
        id, url, region, region_url, price, year, manufacturer, model, condition, 
        cylinders, fuel, odometer, title_status, transmission, VIN, drive, size, 
        type, paint_color, image_url, description, county, state, lat, long, posting_date
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(row))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("Данные успешно загружены в базу данных.")
