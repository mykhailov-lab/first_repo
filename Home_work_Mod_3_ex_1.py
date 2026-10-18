def get_days_from_today(date_1):
    from datetime import datetime

    object_day = datetime.strptime(date_1, '%Y-%m-%d').date() # Перетворення рядка у обєкт
    today_date = datetime.now().date() # Поточна дата

    diff_day = today_date - object_day # Різниця між поточною та заданою датою
    
    return (diff_day.days)

result = get_days_from_today('2024-12-25') # Задана дата

print(f'Кількість днів від заданої дати : {result}')