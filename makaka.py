dic_sentence = {}
sentences = [input("Please enter a sentence: ") for _ in range(3)]

for sentence in sentences:
    for count in sentence:
        if count.isalpha():
            count = count.lower()
            dic_sentence[count] = dic_sentence.get(count, 0) + 1
print("Letter frequencies: ")
for letter, freq in dic_sentence.items():
    print(f"{letter} {freq}")