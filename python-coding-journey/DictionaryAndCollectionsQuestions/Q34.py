# 34. Implement defaultdict example

from collections import defaultdict

word_count = defaultdict(int)

words = ["apple", "banana", "apple"]

for word in words:
    word_count[word] += 1

print(dict(word_count))