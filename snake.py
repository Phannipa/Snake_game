from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Create ate the left position. Put it on the top of the class to be a constant and you have to change to be all capitalized letter.
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self): #Determine what should happen when we initialize
        self.segment =[] #Using self when we're working with class.
        self.create_snake() #Calling method create_snake
        self.head = self.segment[0] # Set head attribute


# Create the snake body
    def create_snake(self):
        for position in STARTING_POSITION: # Each segment is a individual turtle.
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")  # Call class and indicate the shape. Create the turtle at the center positio
        new_segment.color("white")
        new_segment.penup()  # To delete the line
        new_segment.goto(position)
        self.segment.append(new_segment)

# Add a new segment to the snake.
    def extend(self):
        self.add_segment(self.segment[-1].position())


# Move the snake
    def move(self):
     # Figure out a way for the tail of the snake to follow where the head is going
        for seg_num in range (len(self.segment)-1, 0, -1): #len(segment) - 1 = start, 0= stop, -1 = step
            new_x = self.segment[seg_num-1].xcor() # new_x and new_y mean that last index index2) moves to previous index (index 1) by using step
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x, new_y) # means last index will move to the previous index. From this segment list, it will move from index2 to index 1.
        self.head.forward(MOVE_DISTANCE)    # We can write "self.segment[0].forward(MOVE_DISTANCE)"



#Control the snake
    def up(self):
        if self.head.heading() != DOWN: #This heading is a method, Set like this in case that we cannot move to the opposite direction.
            self.head.setheading(UP) #Or we can write self.segment[0].setheading(90). Use self.segment[0] because index: 0 is going to move first.. It's a head of snake and the rest of body will follow it because it's continously moving on every tick of the clock from move function.

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

