print("Welcome to Momo Transaction!")
transaction_type = input("Select transaction type(Send Money/Airtime To)")
amount = float(input("Enter amount: "))
phone_number = input("Enter Recipeint Phone Number: ")

# Simulate confirmation screen
print(f"\n**Confirmation**")
print(f"Transaction Type: {transaction_type}")
print(f"Amount: GHS {amount:.2f}")
print(f"Phone Number: {phone_number}")

confirmation = input("Confirmation Transaction (y/n): ")

if confirmation.lower() == 'y':
    print("Transaction Successful!")
else:
    print("Transacation Cancelled.")
    