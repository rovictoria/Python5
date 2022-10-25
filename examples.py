# Ускоренная обработка данных:
# lambda, filter, map, zip, enumerate, list comprehension

# Анонимные, lambda функции

def f(x):
    return x**2

g = f # переменная хранит ссылку на функцию
print(type(f))
print(g(2))

def calc1(x):
    return x+10
print(calc1(10))

def calc2(x):
    return x*10
print(calc2(10))

#вызов функции в функции
def math(op, x):
    print(op(x))
math(calc2, 10)   
math(calc1, 10)

# если 2 аргумента
# def sum(x,y):
    # return x+y

sum = lambda x, y: x + y  # это же, но лямбда

def mylt(x,y):
    return x*y

def calc(op, a, b):
    print(op(a,b))

calc(sum, 4, 5)
calc(lambda x, y: x + y, 4, 5)

print()

# List Comprehension быстро создавать списки
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

list1 = []
for i in range(1,21):
    if (i% 2 == 0):
        list1.append(i)
print(f'Чётные числа [1,20] вывод через ф-ю: {list1}')

# если просто печать от 1  до 20
list1 = [i for i in range(1,21)]
print(f'Вывод чисел [1,20]: {list1}')

print()

# если с условием только чётные
list1 = [i for i in range(1,21) if i % 2 == 0]
print(f'Чётные числа [1,20]: {list1}')

print()

#если нужны кортежи
list1 = [(i,i) for i in range(1,21) if i % 2 == 0]
print(f'Кортежи чётных чисел [1,20] (i,i): {list1}')
# [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

print()

def f(x):
    return x**3
list1 = [f(i) for i in range(1,21) if i % 2 == 0]
print(f'Кубы чётных чисел [1,20]: {list1}')

print()

#вывод кубов через кортежи число - куб
list1 = [(i,f(i)) for i in range(1,21) if i % 2 == 0]
print(f'Кубы чётных чисел [1,20] (число - куб): {list1}')

print()

# Продолжение Анонимные, лямбда функции
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

f = open('numbers1.txt', 'r')
data = f.read() + ' '  # всё считывается, в конце ставится пробел
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e,e **2))
print(out)

print('А теперь иначе')

def select (f, col):  # функция, данные
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data) 
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
res = filter(lambda x: not x%2, res) #ВМЕСТО WHERE
res = list(map(lambda x: (x, x**2), res))   #ВМЕСТО СЕЛЕКТ
print(res)


# Функция map
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#         ↓   ↓  ↓  ↓   ↓
#      [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

list1 = [x for x in range(1,21)]
list1 = list(map(lambda x: x+10, list1))  #надо превратить в список list(...)
print(list1)


data = list(map(int, input().split(',')))
print (data)
# если не хочется приводить к списку, но так вывод сработает только один раз
# нужно кидать в list
for e in data:  
    print(e)

# Функция filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#  ↓
#  [ 2, 4 ]
# Нельзя пройтись дважды

data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))
print(res)



# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды
users = ['user1', 'user2', 'user3', 'user4']
ids = [4, 5, 9, 14, 7]
salary=[22, 222, 223]
data = list(zip(users, ids, salary))
print(data)
# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

data = list(enumerate(users))
print(data)