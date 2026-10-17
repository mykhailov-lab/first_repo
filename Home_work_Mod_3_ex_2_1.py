import random
def get_random_digits(min, max, un_num):
    new_list = []
    while len(new_list) < un_num :
        b = random.randint(min, max)
        if new_list.count(b) == 0 :
            new_list.append(b)
    new_list.sort()
    return (new_list)
num_1 = int(input('Wwedite "min" chislo:'))
num_2 = int(input('Wwedite "MAX" chislo:'))
num_3 = int(input('Skolko unikalnih chisel :'))
result = get_random_digits(num_1, num_2, num_3)
print(result)