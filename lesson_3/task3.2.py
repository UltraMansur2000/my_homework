nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
        'seven': 'семь', 'eight': 'восемь',
        'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(x):
    if x.lower() in nums:
        if x.islower():
            return nums[x]
        else:
            return nums[x.lower()].title()
    else:
        return None


for num in nums:
    print(num_translate_adv(num))
    print(num_translate_adv(num.title()))
