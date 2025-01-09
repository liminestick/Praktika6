import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка очищенных данных
data = pd.read_csv('vehicles_subset_cleaned.csv')

# Настройки для визуализаций
sns.set(style="whitegrid")

# 1. Линейный график: изменение цен по годам
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='year', y='price', marker='o')
plt.title('Изменение цен по годам')
plt.xlabel('Год')
plt.ylabel('Цена')
plt.show()

# 2. Столбчатый график: распределение по условиям
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='condition', palette='viridis')
plt.title('Распределение автомобилей по состоянию')
plt.xlabel('Состояние')
plt.ylabel('Количество')
plt.show()

# 3. Круговая диаграмма: распределение по типам топлива
fuel_counts = data['fuel'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(fuel_counts, labels=fuel_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Распределение автомобилей по типам топлива')
plt.axis('equal')
plt.show()

# 4. Корреляционная матрица для числовых данных
correlation_matrix = data[['price', 'year', 'odometer']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Корреляционная матрица')
plt.show()

# 5. Гистограмма: распределение цен автомобилей
plt.figure(figsize=(10, 6))
sns.histplot(data['price'], kde=True, color='blue', bins=30)
plt.title('Распределение цен автомобилей')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()

# 6. Ящик с усами (Box plot): пробег автомобилей
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='fuel', y='odometer', palette='Set2')
plt.title('Ящик с усами по пробегу автомобилей')
plt.xlabel('Тип топлива')
plt.ylabel('Пробег')
plt.show()

# 7. Диаграмма рассеяния (scatter plot): зависимость цены от пробега
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='odometer', y='price', color='red')
plt.title('Зависимость цены от пробега')
plt.xlabel('Пробег')
plt.ylabel('Цена')
plt.show()
