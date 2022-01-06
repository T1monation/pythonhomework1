import random


def get_jokes(first, seсond, third, count=1, original=False):
    """
    Joke generator function
    count - number of jokes
    original - False/True repeat word in joke
    """
    i = 0
    joke = []
    if count > len(first):  # В цикле проверяем, если введенное число больше длинны списка слов, приравниваем
        count = len(first)  # счетчик к длинне масива
    if original:
        while i < count:
            if i > 0:
                first.remove(word_1_rm)
                seсond.remove(word_2_rm)
                third.remove(word_3_rm)
                word_1 = first[random.randint(0, len(first) - 1)]
                word_2 = seсond[random.randint(0, len(seсond) - 1)]
                word_3 = third[random.randint(0, len(third) - 1)]
                word_1_rm = word_1  # Список слов на удаление из оригинального списка для избежания повторов шуток
                word_2_rm = word_2
                word_3_rm = word_3
                joke.append(f'{word_1} {word_2} {word_3}')
                i += 1
            else:
                word_1 = first[random.randint(0, len(first) - 1)]
                word_2 = seсond[random.randint(0, len(seсond) - 1)]
                word_3 = third[random.randint(0, len(third) - 1)]
                word_1_rm = word_1
                word_2_rm = word_2
                word_3_rm = word_3
                joke.append(f'{word_1} {word_2} {word_3}')
                i += 1
    else:
        while i < count:
            word_1 = first[random.randint(0, len(first) - 1)]
            word_2 = seсond[random.randint(0, len(seсond) - 1)]
            word_3 = third[random.randint(0, len(third) - 1)]
            joke.append(f'{word_1} {word_2} {word_3}')
            i += 1
    return joke


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes(nouns, adverbs, adjectives, count=10, original=True))
