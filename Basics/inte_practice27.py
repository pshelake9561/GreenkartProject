def char_freq(word):
    word_occurance = {}
    for i in word:
        if i in word_occurance:
            word_occurance[i] += 1
        else:
            word_occurance[i] = 1

    print(word_occurance)
    char_max = None
    char_count = 0
    for char, count in word_occurance.items():
        if count > char_count:
            char_count = count
            char_max = char
    print(f"Max Char Occurence: {char_max} and count is {char_count}")


input_text = input("Enter a text: ")
char_freq(input_text)
