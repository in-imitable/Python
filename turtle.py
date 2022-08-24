# import turtle

# # wn = turtle.Screen()
# # wn.setup(400, 400)

# radius = 60
# # width = 240
# # height = 300

# alex = turtle.Turtle()
# # alex.shape('turtle')
# # alex.color('blue')
# alex.circle(radius)

number = input('Number: ')
sum = 0
while(choice == "y"):
    if(int(number) % 4 == 0):
        print("Do you want to continue? (y/n): ")
        choice = input()
    sum = sum + number

print(sum)
