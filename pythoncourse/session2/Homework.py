# Exercise 11 and 12 #

# age = input("How old are you? ")
#
# height = input("How tall are you? ")
#
# weight = input("How much do you weigh? ")
#
# print('So, you\'re %r old, %r tall and %r heavy.' % (age, height, weight))

# Exercise 13 #

# from sys import argv
#
# script, first, second, third , fourth = argv
#
# print("The script is called:"), script
# print("Your first variable is:"), first
# print("Your second variable is:"), second
# print("Your third variable is:"), third
# print("Give me a fourth variable: "), fourth

# Exercise 14 #

# from sys import argv
#
# script, user_name = argv
# prompt = 'Hmmmm? '
#
# print("Hi %s, I'm the %s script." % (user_name, script))
# print("I'd like to ask you a few questions.")
# print("Do you like me %s?" % (user_name))
# likes = input(prompt)
#
# print("What city do you live in %s?" % (user_name))
# lives = input(prompt)
#
# print("What kind of computer do you have?")
# computer = input(prompt)
#
# print("What part of the city do you live in?")
# city = input(prompt)
#
# print("""
# Alright, so you said %r about liking me.
# You live in %r.  Not sure where that is.
# And you have a %r computer and live in %r.  Nice.
# """ % (likes, lives, computer, city))

# Exercise 18 #

# this one is like your scripts with argv
# def print_two(*args):
#     arg1, arg2 = args
#     print("arg1: %r, arg2: %r" % (arg1, arg2))
#
# # ok, that *args is actually pointless, we can just do this
# def print_two_again(arg1, arg2):
#     print("arg1: %r, arg2: %r" % (arg1, arg2))
#
# # this just takes one argument
# def print_one(arg1):
#     print("arg1: %r" % (arg1))
#
# # this one takes no arguments
# def print_none():
#     print("I got nothin'.")
#
#
# print_two("Zed","Shaw")
# print_two_again("Zed","Shaw")
# print_one("First!")
# print_none()

# Exercise 19 #

# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     """Prints strings with function inputs"""
#     print("You have %d cheeses!" % (cheese_count))
#     print("You have %d boxes of crackers!" % (boxes_of_crackers))
#     print("Man that's enough for a party!")
#     print("Get a blanket.\n")
#
# """Runs function with inputs 20 and 30, respectively"""
# print("We can just give the function numbers directly:")
# (cheese_and_crackers(20, 30))
#
# """Establishes new function inputs and then runs function below"""
# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
# """Runs function with new inputs that perform arithmetic operations inside input"""
# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)
#
# """Takes previous inputs and adds new values"""
# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#
#
# def cracker_sandwiches(amount_of_cheese, amount_of_crackers):
#     """Takes crackers and cheese input and calculates the number of cracker sandwiches you can make."""
#     sandwiches = amount_of_crackers / (amount_of_crackers / amount_of_cheese)
#     print("You can even make %s cracker sandwiches." % int((sandwiches)))
#
# cracker_sandwiches(15, 30)

# Exercise 28 #

# True and True = True
#
# False and True = False
#
# 1 == 1 and 2 == 1 = False
#
# "test" == "test" = True
#
# 1 == 1 or 2 != 1 = True
#
# True and 1 == 1 = True
#
# False and 0 != 0 = False
#
# True or 1 == 1 = True
#
# not (1 == 1 and 0 != 1) = False
#
# not (10 == 1 or 1000 == 1000) = False

# Exercise 30 #

people = 30
cars = 40
trucks = 15

"""Condition to print the statement if the condition is true. If not true, looks to second statement, or to third."""
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")



