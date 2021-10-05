import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

random_name = random.randint(0, len(names)-1)
print(f"{names[random_name]} have to pay a bill.")
#random_name = random.choice(names)
#print(f"{random_name} have to pay a bill.")