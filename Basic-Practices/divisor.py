def divisor(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count +=1
    return count

a = list(map(int, input("Enter 10 numbers: ").split()))

counter_list = {}
for i in a:
    counter_list[i] = divisor(i)


maxi = max(counter_list.values())
for i, j in counter_list.items():
    if j == maxi:
        print(F"number: {i} with {j} divisor")
