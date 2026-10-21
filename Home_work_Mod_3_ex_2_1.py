import random
def get_numbers_ticket(min, max, quantity):
    new_list = []
    if min < 0 or max < 0 or quantity < 0 or max >1000 or min <1 :
        return []
    if min>max: 
        return []
    if (max - min +1 ) < quantity:
        return []
    while len(new_list) < quantity :
        b = random.randint(min, max)
        if new_list.count(b) == 0 :
            new_list.append(b)
    new_list.sort()
    return (new_list)
min = int(input('Wwedite "min" chislo:'))
max = int(input('Wwedite "MAX" chislo:'))
quantity = int(input('Skolko unikalnih chisel :'))
print(get_numbers_ticket(min, max, quantity))