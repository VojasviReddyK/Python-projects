print("Thank you for choosing python pizza deliveries")
size=input("Which size of pizza would you like to have?Small or Medium or Large")
add_pepperoni=input("Would you like to add pepperoni to your pizza?Y or N")
extra_cheese=input("Would you like to have extra cheese on your pizza?Y or N")
bill=0
if size=="Small":
    bill+=15
elif size=="Medium":
    bill+=20
elif size=="Large":
    bill+=25
if add_pepperoni=="Y":
    if size=="Small":
        bill+=2
    else:
        bill+=2
if extra_cheese=="Y":
    bill+=4
print("Your total bill is:",bill)