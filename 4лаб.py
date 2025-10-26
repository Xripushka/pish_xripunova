#1 задача
sentence = "apple banana apple orange banana kiwi"

unique_words = sorted(set(sentence.split()))
print(unique_words)

#2 задача

from collections import Counter
string = "abracadabra"
frequency = Counter(string)
print("Частота символов:", dict(frequency))

#3 задача

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = sorted(set(list1) & set(list2))
print(intersection)

#4 задача

n = 5
squares_dict = {i: i**2 for i in range(1, n + 1)}
print(squares_dict)