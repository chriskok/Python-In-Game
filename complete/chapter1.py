# There are two types of basic variables in Python:
# 1. Numbers
diamonds = 7  # known as an int (integer) or whole number
print(diamonds)
health = 3.5  # known as a float or floating point number
print(health)
health2 = float(3)  # can also declare through conversion from int
print(health2)

# 2. Strings
name = 'Steve'
print(name)
name = "Steve"  # both ways of declaring strings are acceptable
print(name)

# You can name them in a variety of ways:
name = "Steve"
mYnAmE = "Steve"
MYNAME = "Steve"
myName = "Steve"
my_name = "Steve"
_name = "Steve"

# But some naming conventions are illegal:
# 2ndName = "Steve"  # cannot start with numbers
# my-name = "Steve"  # cannot contain a hyphen...
# my name = "Steve"  # or a space in the name

# You can even declare multiple variables together
diamonds, emeralds = 2, 3
print(diamonds,emeralds)

# Variables can be added together and saved
iron = 4
coal = 6
total_ore = iron + coal
print(total_ore)

greeting = "Hello"
person = "Bones"
speech = greeting + " " + person
print(speech)

# However, adding variables of different types is forbidden!
iron = 12
greeting = "Hello"
# print(greeting + iron)

# TODO: Change this code
# Declare your name as "Bob", set your health to 2.0 and 
# set your diamond count to 20
my_name = None
my_health = None
my_diamonds = None

# testing code
if my_name == "Bob":
    print("Name (string): {}".format(my_name))
if isinstance(my_health, float) and my_health == 2.0:
    print("Health (float): {}".format(my_health))
if isinstance(my_diamonds, int) and my_diamonds == 20:
    print("Diamonds (int): {}".format(my_diamonds))