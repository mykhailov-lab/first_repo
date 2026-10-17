from datetime import datetime
date_format = '2024-05-01' # Функція приймає параметр дати

object_day = datetime.strptime(date_format, '%Y-%m-%d').date() # Перетворення рядка у обєкт
today_date = datetime.now().date() # Поточна дата
diff_day = today_date - object_day # Різниця між поточною та заданою датою
print('Кількість днів від заданої дати :', diff_day.days)