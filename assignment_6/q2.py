

def calculator(num1,num2,operation):
    if operation =="add":
        print("sum is : ", num1 + num2)

    if operation == "sub":
        print("sub is : ", num1-num2)

    if operation == "mul":
        print("multiply is : ", num1*num2)

    if operation == "div":
        print("division is : ", num1/num2)

    else:
        print("enter valid opertaion!!")

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))


message = """enter (add) for addition 
enter (sub) for subtraction 
enter (mul) for multiplication 
enter (div) for division """
print(message)
operation = input("enter the operation : ")
calculator(num1,num2,operation)


