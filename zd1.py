import random

lst = []

for _ in range(10):
    lst.append(random.randint(1, 10))

print("Сгенерированный список:", lst)

user_input = int(input("Введите число от 1 до 10: "))

if user_input in lst:
    print(f"Число {user_input} находится в массиве")
else:
    print(f"Число {user_input} не найдено в массиве")
