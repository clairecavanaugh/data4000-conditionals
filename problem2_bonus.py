# Problem 2: Employee Performance Bonus
# Calculates an employee's annual bonus based on their performance score.

# Get inputs from the user
annual_salary = float(input("Enter the annual salary: $"))
performance_score = float(input("Enter the performance score (0-100): "))

# Determine the bonus percentage using score ranges
if performance_score < 0 or performance_score > 100:
    # Scores outside 0-100 are not valid
    print("Invalid score. Please enter a value between 0 and 100.")
    bonus_percent = None
elif performance_score >= 90:
    bonus_percent = 20   # 90-100
elif performance_score >= 80:
    bonus_percent = 10   # 80-89
elif performance_score >= 70:
    bonus_percent = 5    # 70-79
else:
    bonus_percent = 0    # below 70

# Calculate and display the bonus (only if the score was valid)
if bonus_percent is not None:
    bonus_amount = annual_salary * bonus_percent / 100

    print(f"Performance Bonus: {bonus_percent}%")
    print(f"Bonus Amount: ${bonus_amount:,.2f}")
