while True:
    try:
        temperature = float(input("Please input the temperature of water: "))
        if temperature < -273 or temperature > 373:
            print("Its impossible! try again")
            continue
        elif temperature <= 0:
            print("Ice")
            continue
        elif 100 >=temperature >= 0:
            print("Water!")
        else:
            print("steam")
    except ValueError:
        print("Please input a number")
        continue
    except EOFError:
        print("Bye")
        break