# from turtle import Turtle, Screen
# # import turtle  another way to do both actions
#
# # timmy = turtle.Turtle()
# timmy = Turtle()
# timmy.shape("turtle")  # changes image to turtle
# timmy.color("azure4")  # changes color of turtle
# timmy.forward(100)  # will move turtle forward 100 paces
#
# my_screen = Screen()
# my_screen.exitonclick()  # allows program to continue running until clicking on screen

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
