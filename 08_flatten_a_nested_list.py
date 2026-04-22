import itertools

list1 = [[3,4,7],[5,3,7]]

newlist=[]
for list2 in list1:
    for j in list2:
        newlist.append(j)
print(newlist,"method1")

flat_list = list(itertools.chain.from_iterable(list1))
print(flat_list,'method2')

flat_list1 = [i for j in list1 for i in j]
print(flat_list1,'method3')