import csv
from collections import OrderedDict

# Пути к файлам
input_file = '../Downloads/Датасет_для_задания_автоматическая_очистка.csv'
output_file = 'cleaned_dataset.csv'

# Чтение данных
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(f"Исходное количество записей: {len(data)}")

# Столбцы для результата (без ID)
output_columns = ['Age', 'Income', 'Purchase', 'City', 'Gender', 'Last_Purchase_Days', 'Category']

# Удаление полных дубликатов
seen = set()
unique_data = []

for row in data:
    # Создаем кортеж из значений нужных столбцов для проверки уникальности
    row_tuple = tuple(row.get(col, '') for col in output_columns)
    
    if row_tuple not in seen:
        seen.add(row_tuple)
        # Добавляем только нужные столбцы
        unique_row = {col: row.get(col, '') for col in output_columns}
        unique_data.append(unique_row)

duplicates_count = len(data) - len(unique_data)
print(f"Найдено полных дубликатов: {duplicates_count}")
print(f"Количество записей после очистки: {len(unique_data)}")

# Сохранение результата
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=output_columns)
    writer.writeheader()
    writer.writerows(unique_data)

print(f"\n[OK] Очищенные данные сохранены в файл: {output_file}")
print(f"\nПервые 5 строк результата:")
for i, row in enumerate(unique_data[:5], 1):
    print(f"{i}. {row}")

print(f"\nПоследние 5 строк результата:")
for i, row in enumerate(unique_data[-5:], len(unique_data)-4):
    print(f"{i}. {row}")
