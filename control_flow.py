for x in range(2,11,2):
    print(x)

list=[1,10,15,20,45,-12,-12.2,-12.15,10.25]
for x in list:
    if x%2==0:
       print(x)

list_1=[4,9,16,25,72,81,100]
for x in list_1:
  print(x**0.5)

for x in range(0,9,-1):
  print(x)

user=int(input("enter number"))
k=0
for x in range(1,user+1):
  if user%x==0:
    k +=1
if k==2:
   print("prime")