from turtle import Turtle
import random

MYCOLOR = ["yellow", "red", "purple", "orange", "blue"]
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280) #Generating random location for the food in the x-axis.
        random_y = random.randint(-280, 280) #Generating random location for the food in the y-axis
        self.color(random.choice(MYCOLOR))
        self.goto(random_x, random_y)