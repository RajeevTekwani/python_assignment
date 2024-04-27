def palindron(number):
    if number<0:
        print("number is not palindron")
    newnum=0
    original_num=number
    while number>0:
        digit=number%10
        newnum=(newnum*10)+digit
        number=number//10
    if newnum==original_num:
        print("number is palindron")
    else:
        print("number is not palindron")

number=int(input("enter number "))
palindron(number)


