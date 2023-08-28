from turtle import Turtle 
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.new_bits = []
        self.create_snake()
        self.head = self.new_bits[0]

    def create_snake(self):
        for positions in STARTING_POSITION:
            self.add_parts(positions)

    def add_parts(self, positions):
        bit_1 = Turtle("square") #First part of the snake
        bit_1.color("green")
        bit_1.penup()
        bit_1.goto(positions)
        self.new_bits.append(bit_1)

    def extend(self): 
        self.add_parts(self.new_bits[-1].position())

    def moving(self):
        for bit_num in range(len(self.new_bits) - 1, 0, -1):
            x_cor = self.new_bits[bit_num - 1].xcor()
            y_cor = self.new_bits[bit_num - 1].ycor()
            self.new_bits[bit_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self): #If already down, then it is not allowed to go up.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self): #If already up, then it is not allowed to go down.
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self): #If already right, then it is not allowed to go left.
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: #If already left, then it is not allowed to go right.
            self.head.setheading(RIGHT)