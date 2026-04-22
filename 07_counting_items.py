from collections import Counter

fruits = ['apple','banana','kivi','apple','kivi','apple','kivi']
# method1
count_kivi = Counter(fruits).get('kivi')
print(f"Fruit kivi appears in list {count_kivi} times Method1")

count=0
for fruit in fruits:
    if fruit == 'kivi':
        count+=1
print(f"Fruit kivi appears in list {count} times Method2")

