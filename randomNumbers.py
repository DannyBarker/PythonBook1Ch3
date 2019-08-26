import random

my_randoms = list()

for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

numb_list = list(range(1, 11))

for number in numb_list:
    x = False
    for list_Num in my_randoms:
        if list_Num == number:
            x = True
    print(f"My random list {'contains' if x else 'does not contain'} {number}")
