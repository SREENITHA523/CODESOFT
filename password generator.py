import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums='0123456789'
special="@!#$%^&*"
all=lower+upper+nums+special
x=int(input("enter the length of the password"))
password="".join(random.sample(all,x))
print(password)



