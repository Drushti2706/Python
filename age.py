#pip install dateutil

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Get user's birthdate input
birth_input = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d")
    today = datetime.today()

    # Calculate the difference
    age = relativedelta(today, birth_date)

    print("\n--- Age Calculator ---")
    print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
except ValueError:
    print("Invalid format! Please enter date as YYYY-MM-DD.")
