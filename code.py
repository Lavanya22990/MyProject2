# 🎯 A simple Python program to greet you and check your voting eligibility

# 1. Ask the user for their name and greet them
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python.")

# 2. Ask the user for their birth year
birth_year = int(input("What year were you born? "))

# 3. Calculate their approximate age (Assuming the current year is 2026)
current_year = 2026
age = current_year - birth_year
print(f"You are approximately {age} years old.")

# 4. Use an if/else statement to check voting eligibility (Age 18+)
if age >= 18:
    print("✅ You are eligible to vote!")
else:
    years_left = 18 - age
    print(f"❌ You are not eligible to vote yet. You need to wait {years_left} more year(s).")
