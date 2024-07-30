def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        i = i.casefold()
        if root_word.casefold() in i or i in root_word.casefold():
            same_words.append(i)
    return f'Это корень - {root_word}, а это однокоренные слова: {same_words}'


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
