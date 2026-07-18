def calculate_change(bill, paid):
    change = paid - bill
    return change

bill = float(input("Enter the total bill: $"))
paid = float(input("Enter the amount paid: $"))

change = calculate_change(bill, paid)

print("Change to return: $", change)