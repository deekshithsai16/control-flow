person_1="ABC"
person_2="XYZ"
interview={person_1:True,person_2:False}
if interview[person_1]:
	print("welcome to it sector")
else:
	print("go to cooking")
if interview[person_2]:
	print("welcome to it sector")
else:
	print("go to cooking")


#subjects

sai={"telugu":89,"hindi":83,"english":95,"maths":81,"science":70,"social":80}
print(sai)
marks={sai["telugu"],sai["hindi"],sai["english"],sai["maths"],sai["science"],sai["social"]}
print(marks)
print(type(marks))
qualify= set(range(35,100,1))
print(qualify)
res=qualify >= marks
print(res)
if(qualify >= marks):
	print("pass")
else:
	print("fail")