#maya
age = input("please enter your age!")
if int(age) >= 18:
    print("you can view any movie rated R")
elif int(age) >= 13:
    print("you can view pg-13 and pg movies")
else:
    print("you can only watch pg movies")
