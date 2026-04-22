a = [234774,7556456,6786344,45354323]

newlst = ['{:,}'.format(num) for num in a]
print(newlst)

second_lst = [f"{num:_}" for num in a]
print(second_lst)