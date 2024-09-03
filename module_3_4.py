def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for i in other_words:
        other_words = i.lower()
        if root_word_lower in other_words or other_words in root_word_lower:
            same_words.append(i)
    return same_words


print(single_root_words("rich", "richiest", "orichalcum", "cheers", "richies"))
print(single_root_words("Disablement", "Able", "Mable", "Disable", "Bagel"))
