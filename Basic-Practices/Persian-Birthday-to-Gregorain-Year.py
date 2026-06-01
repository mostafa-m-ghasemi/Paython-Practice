day = int(input("What is your birthday date? "))
month = int(input("What is your birthday month? "))
year = int(input("What is your birthday year? "))
gregorian = year
if month < 10 and day <= 10:
    gregorian += 621
else:
    gregorian += 622

print(f"your birthday gregorian year's is : {gregorian}")