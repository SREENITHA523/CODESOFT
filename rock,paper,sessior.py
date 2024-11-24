import random
rock=1
paper=2
scissor=3

user_choice=int(input("enter your choice(1.rock,2.paper,3.scissor):"))
if user_choice>=4 or user_choice<1:
    print("invalid number ,you lose.")
else:
    computer_choice=random.randint(1,3)
    print("computer choice")
    if computer_choice==user_choice:
        print("it's a tie")
    elif computer_choice==1 and user_choice==3:
        print("you lose")
    elif computer_choice==3 and user_choice==1:
        print("you win")
    elif computer_choice>user_choice:
        print("you lose")
    elif computer_choice<user_choice:
        print("you win.")