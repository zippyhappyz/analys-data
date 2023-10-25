import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Hpzilyas2001"
)

query = "SELECT * FROM mtcars;"
data = pd.read_sql_query(query, conn)

total_rows = len(data)
total_rows_and_columns = data.shape
print("Общее количество строк:", total_rows)
print("Количество строк и столбцов:", total_rows_and_columns)

data.info()

unique_models = data['model'].unique()
print("Уникальные модели автомобилей:", unique_models)

most_expensive_car = data.sort_values(by='mpg', ascending=False).iloc[0]
print("Самая дорогая машина:")
print(most_expensive_car)

conn.close()