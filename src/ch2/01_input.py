birth = input("Enter your birthday in the form mm/dd/yyyy: ").strip()
year = birth[6:]
print(f"You were born in the year {year[:4]}.")
