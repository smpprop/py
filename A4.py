def letter_frequency(sentence):
    frequency_dist = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()

        if char in frequency_dist:
            frequency_dist[char] += 1
        else:
            frequency_dist[char] = 1
    return frequency_dist


sentence = input("Enter a Sentence")
result = letter_frequency(sentence)
print(result)
