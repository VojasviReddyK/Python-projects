import random
rock="ROCK"
paper="PAPER"
scissors="SCISSORS"
list=[rock,paper,scissors]
user_choice=int(input("what do you choose? type 0 for rock,1 for paper,2 for scissors"))
computer_choice=random.randint(0,2)
print(computer_choice)
if user_choice>=3 or user_choice<0:
    print("You have typed in an invalid number")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice>user_choice:
    print("You lose")
elif user_choice>computer_choice:
    print("You win")
elif computer_choice==user_choice:
    print("Its a draw")
