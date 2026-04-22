x,y=10,20
print('x is:',x,'y is ',y)
x,y=y,x
print('x is:',x,'y is ',y)

# or we can use XOR (exclusive OR) operator
a,b=1,2

print('a:',a,'b:',b)
a ^= b
b ^= a
a ^= b
print('a:',a,'b:',b)
