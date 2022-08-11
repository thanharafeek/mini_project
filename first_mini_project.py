print("********** welcome to zodiac calculator ***********")
print("enter the number1:")
num1=int(input())
print("enter the number2:")
num2=int(input())
print("these are the operators you can use:")
print("1.Addition")
print("2.Multiplication")
print("3.Division")
print("4.Modulus")
print("5.substraction")
a=input("Please choose an option from these (1,2,3,4,5):")
if a=="1":
    print("Addition")
    print("the sum of the two number is:", num1 + num2)
if a=="2":
    print("Multiplication")
    print("the product of the two number is:", num1 * num2)
if a=="3":
    print("Division")
    print("the divident of the two number is:", num1 / num2)
if a=="4":
    print("Modulus")
    print("the mode of the two number is:", num1 % num2)
if a=="5":
    print("Substraction")
    print("the difference of the two number is:", num1 - num2)
