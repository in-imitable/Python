# This program says hello and asks for my name.

# print('Hello world!')
# print('What is your name?') # ask for their name
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of your name is:')
# print(len(myName))

# print('What is your age?') # ask for their age
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# name = input('Enter your name: ')
# age = int(input('How old are you, {0}? '.format(name)))
# print(age)

# if age >= 18:
#     print("You're eligible to vote")

# else:
#     print("You're not eligible")

class ClassOne:
    __var_one = 1001

    def __init__(self, __var_two):
        self.__var_two = __var_two
        self.__var_five = 5

    def methodOne(self):
        var_four = 50
        self.__var_five = ClassOne.__var_one+self.__var_two+var_four
