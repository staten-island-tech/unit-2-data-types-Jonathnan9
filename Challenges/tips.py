def tip_calculator(bill, rating):
    if rating == 'bad':
        tip_percent = 0
    elif rating == 'okay':
        tip_percent = 0.15
    elif rating == 'good':
        tip_percent = 0.20
    elif rating == 'great':
        tip_percent = 0.25
    else:
        print("Invalid Rating, please pick a valid option")
        rating = input("How was the service? Bad, Okay, Good, Great: ")
        return tip_calculator(bill, rating)  

    tip_amount = tip_percent * bill
    return tip_amount

bill = float(input("Enter the bill amount: $"))
rating = input("How was the service? Bad, Okay, Good, Great: ")
tip = tip_calculator(bill, rating)

if isinstance(tip, str):
    print(tip)
else:
    print("Tip amount: $", round(tip, 2))