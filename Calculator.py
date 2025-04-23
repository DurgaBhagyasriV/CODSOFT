def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2 == 0:
        return "error-Cannot be divided by zero"
    return num1/num2
def modulus(num1,num2):
    return num1%num2
def exponent(num1,num2):
    return num1**num2
while True:
 print("welcome to the calculator !\nThe following operations can be performed:\nAddition\nSubtraction\nMultiplication\nDivision\nModulus\nExponent")
 operation =input("what operation do u want to perform ? ")
 num1=int(input ("enter the first number "))
 num2=int(input ("enter the second number "))
 if operation=="addition":
    print(f"the sum of {num1} and {num2} is: ",addition(num1,num2))
 elif operation=="subtraction":
    print(f"the difference of {num1} and {num2}is: ",subtraction(num1,num2))
 elif operation=="multiplication":
    print(f"the product of {num1} and {num2} is: ",multiplication(num1,num2))
 elif operation=="division":
    print(f"the quotient of {num1} and {num2} is: ",division(num1,num2))
 elif operation=="modulus":
    print(f"the remainder of {num1} and {num2} is: ",modulus(num1,num2))
 elif operation=="exponent":
    print(f"the exponentiation of {num1} and {num2} is: ",exponent(num1,num2))
 else:
     print("invalid operation")
 another_operation=input("do u want to perform other operations ? (yes/no) ")
 if another_operation!="yes":
  print("thank you for using the calculator")
  break
