arr = ['this','is','an','array','of','string']

try:
    iter_check = iter(arr)
except TypeError:
    print("Object a is not itrable")
else:
    print("Object a is itrable")

b=44.5


try:
    iter_check = iter(b)
except TypeError:
    print("Object b is not itrable")
else:
    print("Object b is itrable")