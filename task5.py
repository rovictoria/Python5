# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все
# элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
print('1. Вывод чисел > 5 в последовательности.')
numbers = list(x for x in range(1,11))
print('Первый способ: ')
new_numbers = [i for i in numbers if i > 5]
print(f'Исходная последовательность: {numbers}')
print(f'Все элементы больше 5: {new_numbers}')

print('Второй способ: ')
result_numbers = list(filter(lambda x: x > 5, numbers))
print(f'Все элементы больше 5: {result_numbers}')
print()
# Задача 2. Дан список случайных чисел. Создайте список, в который
# попадают числа, описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
from random import randint

print('2. Случайная возрастающая последовательность из списка: ')

random_numbers = [1, 5, 2, 2, 3, 4, 6, 1, 7]
print(f'Исходная последовательность: {random_numbers}')

def all_larger_numbers(numbers):
    length = len(numbers)
    pos = randint(0, length-2)
    max_length = randint(2, length)
    largers = [numbers[pos]]
    # print(max_length) ДЛЯ ПРОВЕРКИ
    # print(pos)
    k= 0
    if pos > 0:
        while pos!= 0:
            del(numbers[k])
            pos -= 1
    # print(f'Последовательность с выбранной позиции: {numbers}') ДЛЯ ПРОВЕРКИ

    largers = [numbers[pos]] + [i for i in numbers if len(largers) < max_length and i > max(largers)]
    return largers

print(f'Возрастающая последовательность {all_larger_numbers(random_numbers)}')

print()

# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]
import random 

print('3. Удаление повторяющихся элементов в списке, их подсчёт (сколько было суммарно): ')

n = int(input('Введите количество чисел в списке: '))
list1 = [random.randint(1, 10) for _ in range(n)]
length1 = len(list1)  # для 3 способа и аналогично было бы для 2-ого
print(list1)

list_with_counters = [list1.count(i) for i in range(1,11)]
# print(f'Отображение кол-ва повторений чисел [1, 10] соотв-но: {list_with_counters}') #ДЛЯ ПРОВЕРКИ

list_of_repeats = [i for i in list_with_counters if i > 1]
repeats = sum(list_of_repeats)
print(f'Суммарное количество повторений = {repeats}')

print('Первым способом: ')
new_list = []  #чтобы использовать первоначальный список в третьем способе и  в целом по логике
for d in list1:
  if d in new_list: continue
  new_list.append(d)
print(new_list)

print('Вторым способом: ')
print(list(i for (n, i) in enumerate(list1) if i not in list1[0:n]))


