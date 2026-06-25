for i in range(5):
    for j in range(5):
        if j == 2 or i == 0:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
