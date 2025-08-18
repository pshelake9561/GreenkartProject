
def count_of_character_occurances(word):
    words = word.lower()
    word_count = {}
    for i in words:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1

    print(word_count)

input_string = input("Enter a string: ")
count_of_character_occurances(input_string)