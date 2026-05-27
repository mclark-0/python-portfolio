#maya
#functions
def grade_calculator(temperature):
    if temperature > 80:
        print("you should wear sunglasses, shorts, and a short sleeved shirt")
    elif temperature > 60:
        print("you should wear a short sleeved shirt and long pants")
    elif temperature > 40:
        print("you should wear a coat, a long sleeved shirt, and long pants")
    elif temperature > 20:
        print("you should wear a hat, gloves, scarf, and winter coat")
    else:
        print("you should stay inside")
#main
temperature = int(input("please enter the temperature"))
grade_calculator(temperature)
