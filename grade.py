#maya
#functions
def grade_calculator(grade):
    if grade > 90:
        print("you have an A grade")
    elif grade > 80:
        print("you have a B grade")
    elif grade > 70:
        print("you have a C grade")
    elif grade > 60:
        print("you have a D grade")
    else:
        print("you have an F grade")
#main
grade = int(input("please enter your grade"))
grade_calculator(grade)
