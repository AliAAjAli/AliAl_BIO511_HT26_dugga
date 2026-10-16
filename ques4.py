import random 


# a 

results = {"Alice": 0, "Bob": 0, "Draw": 0}

for g in range(20): 
        outcome = random.choice(["Alice", "Bob", "Draw"])
        results[outcome] += 1

print(results) 

# b

first we def a functoin 
then we write a for loop to 