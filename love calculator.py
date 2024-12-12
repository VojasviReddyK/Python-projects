print("The love calculator is calculating your score...")
name1=input("Write your name:")
name2=input("Write your partners name:")
combined_names=name1+name2
lowered=combined_names.lower()
t=lowered.count("t")
r=lowered.count("r")
u=lowered.count("u")
e=lowered.count("e")
first_digit=t+r+u+e
l=lowered.count("l")
o=lowered.count("o")
v=lowered.count("v")
e=lowered.count("e")
second_digit=l+o+v+e
score=int(str(first_digit)+str(second_digit))
if (score<10) or (score>90):
    print("Your score is",score,"you go together like pepsi and mentos")
elif (score>=40) and (score<=50):
    print("Your score is",score,"you are alright together")
else:
    print("Your score is",score)