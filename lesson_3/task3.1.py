nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
        'seven': 'семь', 'eight': 'восемь',
        'nine': 'девять', 'ten': 'десять'}


def num_translate(x):
    if x in nums:
        return nums[x]
    else:
        return None


for num in nums:
    print(num_translate(num))
