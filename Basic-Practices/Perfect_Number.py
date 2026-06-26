while True:
    try:
        perfect = 0
        number = int(input("Please enter a number: "))
        for i in range(1, number):
            if number % i == 0:
                perfect += i
        if perfect == number:
            print("Perfect Number")
        else:
            print("Not a perfect number")
    except ValueError:
        print("Please enter a number")
        continue
    except EOFError:
        print("Bye")
        break