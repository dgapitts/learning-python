from collections import Counter

words = []
for i in range(int(input())):
    w = input()
    words.append(w)

print(len(Counter(words).keys()))

#for word in words:
#     print (word)

print(
    *Counter(words).values()
)