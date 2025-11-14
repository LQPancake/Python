def get_longer_word(word1, word2):
    if len(word1) > len(word2):
        return word1
    elif len(word1) < len(word2):
        return word2
    else:
        return "egyforma"
    