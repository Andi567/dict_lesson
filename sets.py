# Множество в Python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.

# Создание множества 
# Способ №1 - с помощью функции set()
a1 = set("hello")
print (a1)  # Выводится только неповторяющиеся символы

# Способ №2 - с помощью литерала {}
a2 = {'23' : 32}    # Не путать со словарем
a3 = {'23' , 32}    # Между значениями запятая, а не двоеточие
print(a3)

# Способ №3 - с помощью генератора множеств
a4 = {a ** 2 for a in range(7)}
print (a4)

# Заметка - если указать пустые скобки, то типом будет словарь, а не множество
a5 = {}
print (type(a5))
# Для создания пустого множества:
a6 = set()
print (type(a6))

# Также можно создавать неизменяемые множества
a7 = frozenset("qwerty")
print(a7)
# a7.add (1) # Добавлять элементы в него нельзя


# Полезное свойство множеств - удаляются все повторяющиеся значения
a8 = ['o', 'e', 'r', 'a', 'o', 'a'] # Список с символами
print (set(a8)) # Без повторяющихся символов


# Методы множеств
a9 = {32, 45, 43.5, 76}
print (len(a9)) # Длина множества

x1 = 45
print (x1 in a9)  # Проверяет, есть ли Х в множестве A

a = {32, 45, 43.5, 76}
b = {10, 2, 15}
print (a.isdisjoint(b))   # Возвращает True, если 2 множества не имеют общих элементов
print (a == b)            # Проверяет, что ВСЕ элементы множества есть в другом

a.update(b)       # Добавляет в множество А элементы из B       
print(a)

a = {32, 45, 43.5, 76}
b = {32, 10, 2, 15}
a.intersection_update(b)
print (a)   # Общие элементы 2х множеств

a = {32, 45, 2, 76}
b = {32, 10, 2, 15}
a.difference_update(b)
print(a)    # Уникальные элементы множества А (нету в В)

a = {32, 45, 2, 76}
b = {32, 10, 2, 15}
a.symmetric_difference_update(b)
print(a)    # Неповторяющиеся элементы в множествах А и В

a = {32, 45, 2, 76}
b = {32, 10, 2, 15}

a.add (22)      # Добавление элемента
a.remove(32)    # Удаление элемента
a.discard(1)    # Удаляет элемент, если он есть. Использовать его для избежания ошибок! 
print (a)

a.pop()         # Удаляет 1й элемент множества (рандом, так как элементы в случайном порядке)
print (a)      

a.clear         # Удаляет все элементы множества

# ЗАДАНИЕ

with open('4_vera.tsv') as f:
    for line_number, line_data in enumerate(f):
        if line_number == 0:
            continue
        student_id, account_created, last_active, balance, language_id = line_data.rstrip('\n').split('\t')

# Вывести список языков в файле, используя методы множеств