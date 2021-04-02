
def calc_chance(list, words):
    res = 1
    for i in list:
        res *= words.count(i) / len(words)
    return res


word = input("Введите слово: ")
vocabulary = ''.join(["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"])
chars = [i for i in word]

print(calc_chance(chars, vocabulary))


