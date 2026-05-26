def myfunc():
    while True:
        name = input("Enter your name: ")
        upper_case = 0
        lower_case = 0
        for i in name:
            if i.isupper():
                upper_case += 1
            elif i.islower():
                lower_case +=1
        print(f"upper case : {upper_case}")
        print(f"Lower case : {lower_case}")

myfunc()