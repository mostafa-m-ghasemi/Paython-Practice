while True:
    try:
        num = int(input("Enter a number: "))
        number = num
        factorial = 1
        while num > 0:
            factorial *= num
            num -= 1
        print(f" {number}! = {factorial}")
    except ValueError:
        print("Invalid input")
        continue
    except EOFError:
        break
