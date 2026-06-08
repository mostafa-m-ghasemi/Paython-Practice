while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        gcb = 0
        for i in range(num1, 1, -1):
            if num1 % i == 0 and num2 % i == 0:
                gcb = i
                break
        print(gcb)
    except ValueError:
        print("Please enter a number")
        continue
    except EOFError:
        break

