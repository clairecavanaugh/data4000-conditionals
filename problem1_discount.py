# Problem 1: Customer Discount Eligibility
# Determines a customer's discount based on membership status and purchase amount.

# Thresholds and rates stored as named constants so the rules are easy to update
MEMBER_THRESHOLD = 100.00
NON_MEMBER_THRESHOLD = 150.00
MEMBER_HIGH_DISCOUNT = 15
MEMBER_LOW_DISCOUNT = 5
NON_MEMBER_DISCOUNT = 10

# Get inputs from the user
purchase_amount = float(input("Enter the purchase amount: $"))
membership_status = input("Is the customer a member? (yes/no): ").strip().lower()

# Determine the discount percentage
if membership_status == "yes":
    # Members get a larger discount on purchases of $100 or more
    if purchase_amount >= MEMBER_THRESHOLD:
        discount_percent = MEMBER_HIGH_DISCOUNT
    else:
        discount_percent = MEMBER_LOW_DISCOUNT
elif membership_status == "no":
    # Non-members only get a discount on purchases of $150 or more
    if purchase_amount >= NON_MEMBER_THRESHOLD:
        discount_percent = NON_MEMBER_DISCOUNT
    else:
        discount_percent = 0
else:
    # Anything other than yes/no is treated as invalid input
    print("Invalid membership status. Please enter 'yes' or 'no'.")
    discount_percent = None

# Calculate and display the results (only if the input was valid)
if discount_percent is not None:
    discount_amount = purchase_amount * discount_percent / 100
    final_price = purchase_amount - discount_amount

    print(f"Discount applied: {discount_percent}%")
    print(f"Final price: ${final_price:,.2f}")
