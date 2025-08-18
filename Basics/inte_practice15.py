
str = "Automation world"
def count_vowels():
    vowels = "aeiou"
    vowels_count = 0
    consonants_count = 0
    text_lower = str.lower()
    text_lower = "".join(text_lower.split())
    for char in text_lower:
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    print("Vowels count: ", vowels_count)
    print("Consonants count: ",consonants_count)

count_vowels()














