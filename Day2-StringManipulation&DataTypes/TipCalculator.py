print("Welcome to the Tip Calculator.")
totalBill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give?"))
split = int(input("How many people to split the bill?"))
tipAmt = (totalBill * tip) / 100
billaftertip = totalBill + tipAmt
splitAmt = round(float(billaftertip / split), 2)
print("Each person should pay: ", splitAmt)
