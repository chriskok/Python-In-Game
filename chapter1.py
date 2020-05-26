print("hello world!")

villager_name = 'Bones'
emeralds = 0
raw_chickens = 30

# Let's speak to the Butcher named Bones
print("Hi, " + villager_name + "! I'll trade ya 7 raw porkchops for 1 emerald.")
# He tells you he's not looking for that right now

print("Ahh that's too bad, " + villager_name + "... Do you want any raw chickens?")
# He says YES!

print("Perfect! How many raw chickens for 2 emeralds? I have about " + str(raw_chickens) + ".")
# He does the math and tells you that'll be 28 chickens

print("Alright, " + villager_name + ", you have yourself a deal! I'll be left with " + str(raw_chickens - 28) +
      " chickens for myself and 2 whole emeralds richer!")
# You're now 2 emeralds richer!

def