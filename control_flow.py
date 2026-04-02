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

Data={9381732559:"deekshith",3255995022:"sai",3255981793:"rani",8143800804:"sai",123598143:"tharun"}
User="admin"
Password="admin@123"
Login_name=input("enter employee name")
password=input("enter password")
if(Login_name == User) and (password == Password):
	print("Login successful.....")
	acc=int(input("enter acc no: "))
	for x in Data:
		if(x == acc):
			print("acc no: ",x,"name: ",Data[x])