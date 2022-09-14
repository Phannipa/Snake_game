from turtle import Turtle # The food on screen is a Turtle class
import random

#Create the food


class Food (Turtle): # class Food inherit from Turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # size is 10x10 (10%2 = 5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self): #method for food moves random
        random_x = random.randint(-280, 280)  # screen (width =600, length =600).

        # It means a half of x and y are 300 on the right and -300 on the left.
        # We set at 280 and 280 because if we set at -300 and 300, the food will be on the edge of the screen.

        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
