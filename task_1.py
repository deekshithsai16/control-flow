#getting string from user
li=eval(input())
print(type(li))
for i in li:
	i=li[0]
	print(i)
for j in li:
	j=li[1]
	print(j)
for k in li:
	k=li[2]
	print(k)
a=li[0]
print(a)
b=li[1]
print(b)
c=li[2]
print(c)
if a>b and a>c:
	print("a is biggest")
elif b>c:
	print("b is biggest")
else:
	print("c is biggest")