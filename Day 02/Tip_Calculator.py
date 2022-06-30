
print("Welcome to the tip calculator.")

bill = input("What was the total bill ? $")

tip = input("\nHow much tip would you lie to give in % ? 10, 12, 15 ? - ")

people = input("How many people to split the bill ? ")

actual_tip = int(tip) / 100

added_bill = float(bill) * actual_tip

actual_bill = float(bill) + added_bill

person_pay = actual_bill / float(people)

print("each person have to pay $" + str(round(person_pay, 2)))