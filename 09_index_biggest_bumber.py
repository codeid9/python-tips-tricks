x = [45,33,87,112,43,5,10,43,227]

max_num = max(enumerate(x, start=0), key = lambda x:x[1])
print('Index of The largest number is :',max_num[0])