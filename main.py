import pandas as pd
import numpy as np

# Создаем данные
np.random.seed(42)  # для воспроизводимости результатов
students = ['Иван', 'Мария', 'Петр', 'Анна', 'Сергей', 'Наталья', 'Алексей', 'Елена', 'Дмитрий', 'Ольга']
subjects = ['Математика', 'Физика', 'Химия', 'Литература', 'История']

# Генерируем случайные оценки от 2 до 5
data = {subject: np.random.randint(2, 6, size=10) for subject in subjects}

# Создаем DataFrame
df = pd.DataFrame(data, index=students)

# Выводим первые 5 строк для проверки
print(df.head())

# Средний балл по каждому предмету
print("\nСредний балл по предметам:")
print(df.mean())

# Вычисляем медианную оценку по каждому предмету
median_scores = df.median()
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print("\nQ1 для математики:", Q1_math)
print("Q3 для математики:", Q3_math)

# Рассчитываем IQR (межквартильный размах)
IQR_math = Q3_math - Q1_math
print("\nIQR для математики:", IQR_math)

# Вычисляем стандартное отклонение по каждому предмету
std_dev = df.std()
print("\nСтандартное отклонение по предметам:")
print(std_dev)