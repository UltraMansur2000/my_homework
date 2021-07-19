dictionary = {}


def thesaurus(*args):
    for name in args:
        if dictionary.get(name[0]) is None:
            dictionary[name[0]] = [name]
        else:
            dictionary[name[0]].append(name)


thesaurus("Иван", "Мария", "Петр", "Илья")

print(dictionary)
