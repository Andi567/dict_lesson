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
for language in sorted(author):
    print (language," - ",author[language])

print (sorted(author))