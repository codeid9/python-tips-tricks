import sys

a = ['python','laptop','pc','keyboard','mouse']
b = {'python','laptop','pc','keyboard','mouse'}
c = ('python','laptop','pc','keyboard','mouse')

print(f"Memory of list:{sys.getsizeof(a)} \nMemory of set:{sys.getsizeof(b)} \nMemory of tuple:{sys.getsizeof(c)}")