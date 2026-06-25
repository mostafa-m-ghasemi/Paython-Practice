import random

#random.random()
val1 = random.random()
print(f"1 . random.random() return a random float in range [0.0, 1.0). example:  {val1}")
print()

#random.uniform(a, b)
val2 = random.uniform(1.5, 10.3)
print(f"2 . random.uniform() return a random float such that a <= N <= b. example:  {val2}")
print()

#random.randint(a, b)
val3 = random.randint(1, 10)
print(f"3. random.randint() return a random integer such that a <= N <= b. example:  {val3}  ")
print()

#random.randrange(start, stop, step)
val4 = random.randrange(1, 100, 2)
print(f"4. random.randrange() return a randomly element from range(start, stop, step). example:  {val4}")
print()
