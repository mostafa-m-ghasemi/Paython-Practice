print("You can exit the calculator by CTRL + D")
while True:
    try:
        operator = int(input("please enter '1' for '+' and '2' for '-' and '3' for '*' and '4' for '/' and '5' for exit: "))
        if operator == 1 or operator == 2 or operator == 3 or operator == 4:
            number1  = float(input("please enter a number1: "))
            number2 = float(input("please enter a number2: "))
            match operator:
                case 1:
                    print(f"{number1} + {number2} = {number1 + number2}")
                    continue
                case 2:
                    print(f"{number1} - {number2} = {number1 - number2}")
                    continue
                case 3:
                    print(f"{number1} * {number2} = {number1 * number2}")
                    continue
                case 4:
                    print(f"{number1} / {number2} = {number1 / number2}")
                    continue
                case 5:
                    print("Good Bye")
                    break
        elif operator == 5:
            print("good bye")
            break
        else:
            print("please enter a number between 1 and 5")
            continue
    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("you can't divide by zero")
        continue
    except EOFError:
        print("program ended")
        break
