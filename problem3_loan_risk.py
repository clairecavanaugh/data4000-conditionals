# Problem 3: Loan Risk Classification
# Classifies a loan applicant as Low, Medium, or High risk
# based on credit score and annual income.

# Minimum requirements for each risk tier
LOW_RISK_CREDIT = 720
LOW_RISK_INCOME = 60000
MEDIUM_RISK_CREDIT = 650
MEDIUM_RISK_INCOME = 40000

# Get inputs from the user
credit_score = int(input("Enter the credit score: "))
annual_income = float(input("Enter the annual income: $"))

# Check the strictest tier first. An applicant must meet BOTH
# conditions in a tier to qualify for it.
if credit_score >= LOW_RISK_CREDIT and annual_income >= LOW_RISK_INCOME:
    risk_category = "Low Risk"
elif credit_score >= MEDIUM_RISK_CREDIT and annual_income >= MEDIUM_RISK_INCOME:
    risk_category = "Medium Risk"
else:
    # Everyone who doesn't meet Low or Medium requirements
    risk_category = "High Risk"

print(f"Loan Risk Category: {risk_category}")
