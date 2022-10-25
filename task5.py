# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все
# элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

numbers = list(x for x in range(1,11))
new_numbers = [i for i in numbers if i > 5]
print(f'Исходная последовательность: {numbers}')
print(f'Все элементы больше 5: {new_numbers}')

# Задача 2. Дан список случайных чисел. Создайте список, в который
# попадают числа, описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

random_numbers = [1, 5, 2, 2, 3, 4, 6, 1, 7]
def get_up2(random_numbers):
    ups = [random_numbers[0]]
    for i in random_numbers:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(random_numbers))

def get_up(random_numbers):
    ups = []
    for i in range(len(random_numbers)):
        if random_numbers[i] == max(random_numbers[:i+1:]) and random_numbers[i] not in ups:
            ups.append(random_numbers[i])
    return ups

print(get_up(random_numbers))

# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]
import random

n = int(input('Введите количество чисел в списке: '))
list1 = [random.randint(1, 10) for _ in range(n)]
# length1 = len(list1)  # для 3 способа и аналогично было бы для 2-ого
print(list1)

print('Первым способом: ')
list2 = list(set(list1))
print(list2)
# print(f'Количество повторяющихся элементов: {len(list1)-len(list2)}')

print('Вторым способом: ')
new_list = []  #чтобы использовать первоначальный список в третьем способе и  в целом по логике
for d in list1:
  if d in new_list: continue
  new_list.append(d)

list1[:] = new_list
print(list1)

print('Третьим способом: ')
print(list(i for (n, i) in enumerate(list1) if i not in list1[0:n]))
# print(f'Количество повторяющихся элементов: {length1 -len(list1)}')  #для второго аналогичная запись, не дублировала

from collections import Counter
for i in list1:
    c += counter(list1[(i)])
print(Counter(list1))
# Задача 4*. Создайте игру в крестики-нолики.