replace=""
print("********** welcome to zodiac calculator ***********")
print("enter the number1:")
num1=int(input())
print("enter the number2:")
num2=int(input())
print("these are the operators you can use:")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
result=0
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=="1":
    result=num1+num2
    print("The result of addition of",num1,"and",num2,"is",result)
if operator=="2":
    if num1<num2:
        print("cannot subtract because the first number is less than the second")
    else:
        result=num1-num2
        print("The result of subtraction of", num1, "and", num2, "is", result)
if operator=="3":
    if num2==0 or num1==0:
        print("Cannot multiply by zero")
    else:
        result=num1*num2
        print("The result of multiplication of",num1,"and",num2,"is",result)
if operator=="4":
    if num2==0:
        print("cannot divide by zero")
    else:
        result=num1//num2
        print("The result of Division of",num1,"and",num2,"is",result)
if operator=="5":
    if num2==0:
        print("connot work modulus operator")
    else:
        result=num1%num2
        print("the result of modulus of",num1,"and",num2,"is",result)



