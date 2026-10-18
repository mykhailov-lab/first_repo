def get_random_digits(num_1, num_2, num_3):
    import random
    new_list = []
    while len(new_list) < num_3 :
        b = random.randint(num_1, num_2)
        if new_list.count(b) == 0 :
            new_list.append(b)
    new_list.sort()
    return (new_list)
num_1 = int(input('Wwedite "min" chislo:'))
num_2 = int(input('Wwedite "MAX" chislo:'))
num_3 = int(input('Skolko unikalnih chisel :'))
print(get_random_digits(num_1, num_2, num_3))