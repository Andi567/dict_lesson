# Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу. 
# Их иногда ещё называют ассоциативными массивами или хеш-таблицами.

# Создание словаря
# Способ №1 - с помощью литерала {}

d1 = {'test1' : 1, 'test2' : 'TEST'}
print (d1['test1']) # Выведется 1
print (d1)          # Выведется весь словарь 

# Способ №2 - с помощью функции dict()

d2 = dict(short='dict', long='dictionary')
d2['short'] = 123   # Можем менять значение по ключу
print (d2)

# Другая форма задания словаря - из списка с кортежами
d3 = dict ([(12,13), (14,15)])   # ([(ключ, значение), (ключ, значение)])   
print (d3)                      

# Способ №3 - с помощью метода dict.fromkeys()
d4 = dict.fromkeys(['a', 'b'],1)    # создает словарь с 2мя ключами и им всем присваивает 1
print (d4)

# Способ №4 - с помощью генераторов словарей
d5 = {a: a ** 2 for a in range(7)}
print (d5)


# Пример применения
person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'}, 
        'address': ['г. Москва', 'ул. Васильковская д. 23б', 'кв.12'], 
        'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}
        }
print(person['name']['first_name']) # Иван
print (person['address'][1])        # ул. Васильковская д. 23б

person['phone']['mobile_phone'] = '8-987-654-32-10' # Значения можно менять
print (person['phone']['mobile_phone'])
#print (person.keys ())

# Методы словарей (все методы в dict_methods.txt)
print (person.values()) # Возвращает значения словаря
print (person.keys())   # Возвращает ключи в словаре
print (person['name'].values()) # Можно забирать значения вложенного словаря

val1 = person['name'].pop('middle_name')   # Удаляет ключ и значение из словаря и сохраняет занчение в переменную
val2 = person['name'].get('middle_name')   # Возвращает значение по ключу
if val2 != None:  
    print('Ключа middle_name нет')  # Если ключа нет, get() возвращает None

#print(person['name']['middle_name'])    # Это вызовет ошибку, лучше пользоваться get()


# ЗАДАНИЕ
# Имеется словарь
author = {"php":"Rasmus Lerdorf",
        "perl":"Larry Wall",
        "tcl":"John Ousterhout",
        "awk":"Brian Kernighan",
        "java":"James Gosling",
        "parrot":"Simon Cozens",
        "python":"Guido van Rossum"
        }

# Необходимо вывести пары ключ - значение в алфавитном порядке ключа
# Сначала awk  -  Brian Kernighan, java  -  James Gosling и т.д.
