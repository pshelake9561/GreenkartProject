
def word_occurrence(words):
    st_lower = words.lower()
    st_lower = st_lower.split()
    word_count = {}
    for word in st_lower:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)

sentence = input("Enter a sentence: ")
word_occurrence(sentence)