def prime_number():
    try:
        number = int(input("Enter a number: "))
        if number <= 0:
            return "Your number should be greater than 0!!"
        elif number == 1:
            return "Prime"
        else:
            for i in range(2, number):
                if number % i == 0:
                    return "Not prime"
            return "Prime"
    except ValueError:
        return "Please enter a number!!"

while True:
    print(prime_number())