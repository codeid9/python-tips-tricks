from collections import Counter

a='lost'
b='tsol'
# method1
print(Counter(a)==Counter(b))

# method2
if sorted(a)==sorted(b):
    print('Anagram')
else:
    print('Not Anagram')
