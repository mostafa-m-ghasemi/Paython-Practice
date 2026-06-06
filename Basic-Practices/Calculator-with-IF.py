while True:
    try:
        print("You can exit the caculator by CTRL + D")
        number1 = float(input("Please enter a number1: "))
        operator = input("Please enter an operator: '+' or '-' or '*' or '/':  ")
        number2 = float(input("Please enter a number2: "))
        if operator == "+":
            print(f"{number1} + {number2} = {number1 + number2}")
            continue
        elif operator == "-":
            print(f"{number1} - {number2} = {number1 - number2}")
            continue
        elif operator == "*":
            print(f"{number1} * {number2} = {number1 * number2}")
            continue
        elif operator == "/":
            print(f"{number1} / {number2} = {number1 / number2}")
            continue
        else:
            print(f"invalid operator!")
            continue
    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("you can't divide by zero")
        continue
    except EOFError:
        print("program ended")
