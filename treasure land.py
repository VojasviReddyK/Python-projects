print("Welcome to treasure land")
print("Your mission is to find the treasure")
direction=input("Which direction do you want to go left or right?")
if direction=="left":
    action=input("You've reached the lake.Do you want to swim or wait?\n")
    if action=="wait":
        door=input("You've reached the island.There is a house with three doors.Which door do you want to open? red blue or yellow?")
        if door=="red":
            print("Burned by fire.Game over")
        elif door=="blue":
            print("Eaten by beasts.Game over")
        elif door=="yellow":
            print("You win")
    else:
        print("Attacked by trout.Game over")
else:
    print("Fell into a hole.Game over")
