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

else:
     print("invalid user or passwor")