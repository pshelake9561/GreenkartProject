para = "What is the difference between a list and a tuple? What are Python’s built-in data types?"
#para = para.lower()
#words = para.replace(", . ?", " ")
words = para.split()
words_count={}
for i in words:
    if i in words_count:
        words_count[i] += 1

    else:
        words_count[i] = 1


print(words_count)