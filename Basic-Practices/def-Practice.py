
def prime_num(number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
count = 0
b = int(input("Enter a number to show prime numbers between 1 to your number: "))
for i in range(2, int(b ** .5) + 1):
    if prime_num(i):
        count +=1
        print(i)
print(f"{count} prime numbers")
