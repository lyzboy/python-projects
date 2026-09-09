def pig_latin(sentence):
    words = sentence.split(" ")
    pig_latin_sentence = ""
    for word in words:
        pig_latin_sentence += pig_latin_word(word)+" "
    return (pig_latin_sentence.strip())

def pig_latin_word(word):
    if not isinstance(word, str):
        return "Word must be a string"
    vowels = ['a','e','i','o','u']
    if word[0] in vowels:
        return f"{word}-way"
    
    word_list = list(word);
    first_letter = word_list.pop(0)
    return "".join(word_list) + f"-{first_letter}ay"

if __name__ == '__main__':
    print(pig_latin("Well it looks like that works"))