def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.casefold() in word.casefold() or word.casefold() in root_word.casefold():
            same_words.append(word)
    print(same_words)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies' )
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
