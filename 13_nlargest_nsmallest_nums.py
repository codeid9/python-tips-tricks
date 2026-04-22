import heapq

nums = [34,54,67,89,81,23,43,44,49,71,19,46,56,80]
# method1
def large_5_num(lst):
    a = sorted(lst,reverse=True)
    return a[:5]
print(large_5_num(nums))

# method2 
print(heapq.nlargest(5,nums))
print(heapq.nsmallest(5,nums))