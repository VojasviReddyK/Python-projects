print("Welcome to the tip calculator")
bill=float(input("Enter the total bill:"))
tip=int(input("How much percentage of tip would you like to give?"))
split=int(input("How many people are going to split the bill:"))
bill_with_tip=(tip/100)*bill+bill
split_amount=bill_with_tip/split
print("Everyone should pay",split_amount,"Thank you")