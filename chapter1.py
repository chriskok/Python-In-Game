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
      " chickens for myself and 2 whole emeralds richer!\n")
# You're now 2 emeralds richer!


# After asking around some more, you find out the conversion rates for all meats traded
chickens_per_emerald = 14
rabbits_per_emerald = 4
porkchops_per_emerald = 7


# Knowing the conversion rate, let's see how many more chicken
def chickens_to_emeralds(number_of_chickens):
    # print("We have: " + str(number_of_chickens) + " chickens")
    # print("It costs: " + str(chickens_per_emerald) + " for one emerald")

    emeralds_earned = number_of_chickens/chickens_per_emerald
    # print("That means we can get: " + str(emeralds_earned) + " emeralds!")
    return emeralds_earned


profit = chickens_to_emeralds(70)
print("Emeralds from chickens: " + str(profit))


# ASSIGNMENT: How many emeralds can you earn in total?
def total_emeralds(number_of_chickens, number_of_rabbits, number_of_porkchops):
    # TODO: fix the formula to output the total number of emeralds earned if you sold all your raw meat
    # TODO: for now, don't worry about negative numbers or the fact that we get a decimal number of emeralds
    emeralds_earned = 1.0
    return emeralds_earned


profit = total_emeralds(35, 20, 8)
print("Emeralds from all raw meat: " + str(profit))
