word = "Automation"
words = word.lower()
word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

print(word_count)

def words_occurence_count(para):
    words = para.lower()
    words_count = {}
    for i in words:
        if i in words_count:
            words_count[i] +=1
        else:
            words_count[i] = 1

    print(words_count)

    