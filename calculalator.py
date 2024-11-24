
add=print("1.addition")
sub=print("2.substraction")
mul=print("3.multiplication")
div=print("4.divison")
sqre=print("5.square")
num1=int(input("enter the value"))
num2=int(input("enter the value"))
operator=input("enetr an operator")
if(operator=="1"):
    result=num1+num2
    print(result)
elif(operator=="2"):
    result=num1-num2
    print(result)
elif(operator=="3"):
    result=num1*num2
    print(result)
elif(operator=="4"):
    result=num1/num2
    print(result)
elif (operator=="5"):
    result1=num1**2
    result2=num2**2
    print("sqre  of",(num1),result1  )
    print("sqre  of",(num2),result2  )
else:
    print("u entered an invalid operation dear")