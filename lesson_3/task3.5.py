from random import randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    jokes = []
    for i in range(n):
        first_word = nouns[randint(0, len(nouns) - 1)]
        second_word = adverbs[randint(0, len(adverbs) - 1)]
        third_word = adjectives[randint(0, len(adjectives) - 1)]
        jokes.append(' '.join([first_word, second_word, third_word]))
    return jokes


print(get_jokes(3))
