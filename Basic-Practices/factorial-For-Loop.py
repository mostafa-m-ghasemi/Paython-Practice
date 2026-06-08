while True:
    try:
        num = int(input("Enter a number: "))
        factorial = 1
        for i in range(num, 1, -1):
            factorial *= i
        print(f"{num}! = {factorial}")
    except ValueError:
        print("Invalid input")
        continue
    except EOFError:
        break