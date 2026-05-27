#maya
def even():
    while True:
        try:
            user = int(input("enter a number: "))
            if user < 2:
                print("please enter a number greater than or equal to 2 ")
            else:
                break
        except ValueError:
            print("invalid number. please enter an integer ")
    print("Even numbers from 2 to {user}:")
    for i in range(2, user + 1, 2):
        print(i)
even()
