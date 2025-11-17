def change_vowels(word):
    vowels = "aáeéiíoóöőuúüű"
    result = ""
    for character in word:
        if character in vowels:
            result += "."
        else:
            result += character
    return result