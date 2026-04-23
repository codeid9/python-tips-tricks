dict1 = {"name":"john","age":45,"student":False}
print("using comprehension :",{key for key in dict1.keys()})
print("using set:",set(dict1))
print("using sorted:",sorted(dict1))