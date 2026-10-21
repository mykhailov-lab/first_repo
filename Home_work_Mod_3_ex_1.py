from datetime import datetime
def get_days_from_today(date):
    try:
        object_day = datetime.strptime(date, '%Y-%m-%d').date() # Перетворення рядка у обєкт
        today_date = datetime.now().date() # Поточна дата

        diff_day = today_date - object_day # Різниця між поточною та заданою датою
    
        return (diff_day.days)
    except ValueError:
        print('YYYY-MM-DD Неправильний формат!')
result = get_days_from_today('2021-10-09') # Задана дата

print('Кількість днів від заданої дати :' , result)