import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Hpzilyas2001"
)

query = "SELECT * FROM mtcars;"
data = pd.read_sql_query(query, conn)

# Осмотр данных:
print(data.head())  # Первые 5 строк
print(data.tail())  # Последние 5 строк

# Статистическое описание:
print(data.describe())

# Визуализация данных:
plt.hist(data['mpg'], bins=10, color='blue')
plt.xlabel('mpg')
plt.ylabel('Частота')
plt.title('Гистограмма миль на галлон')
plt.show()

# Обработка пропущенных значений:
print(data.isnull().sum())  # Количество пропущенных значений в каждом столбце

# Исследование взаимосвязей:
correlation_matrix = data.corr()
print(correlation_matrix)

conn.close()