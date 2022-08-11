flag=False
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
    replace1="Addition"
    result=num1+num2
if operator=="2":
    if num1<num2:
        flag=False
        print("cannot subtract the first number is less than the second")
    else:
      flag=True
      replace1="subtraction"
      result=num1-num2
if operator=="3":
    replace1="multiplication"
    result=num1*num2
if operator=="4":
    replace1="division"
    result=num1//num2
if operator=="5":
    replace1="modulus"
    result=num1%num2
if flag==True:
    print("the result of",replace1,"of",num1,"and",num2,"is",result)
