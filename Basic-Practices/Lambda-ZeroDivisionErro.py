while True:
    split = lambda bill, persons: bill / persons
    try:
        print(f"Each pays: {split(float(input("Enter the bill: ")), float(input("Enter the persons: "))):.2f}")
        break
    except ZeroDivisionError:
        print("Number of persons can not be zero")
    except ValueError:
        print("invalid input")