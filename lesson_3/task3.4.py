dictionary = {}
sorted_dictionary = {}


def thesaurus_adv(*args):
    for name in args:
        name_letter = name[0]
        surname_letter = name.split()[-1][0]
        if dictionary.get(surname_letter) is None:
            dictionary[surname_letter] = {name_letter: [name]}
        elif dictionary[surname_letter].get(name_letter) is None:
            dictionary[surname_letter].update({name_letter: [name]})
        else:
            dictionary[surname_letter][name_letter].append(name)

    list_keys = list(dictionary.keys())
    list_keys.sort()
    for key in list_keys:
        sorted_dictionary[key] = dictionary[key]
    return sorted_dictionary


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
