import random

exampl_list = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
#random.choice(seq)
print(f"random.choice(seq) return a random element from a none empty sequence. example:  {random.choice(exampl_list)}")
print()

#random.choices(population, k)
print(f"random.choices(population, k) return a list of k random elements from a population\nwith replacement. example:  {random.choices(exampl_list, k=3)}")
print()

#random.sample(population, k)
print(f"random.sample(population, k) return a list of k uniq elements from population sequence. example:  {random.sample(exampl_list, k=3)}")
print()
