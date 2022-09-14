from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

import time

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# tim = Turtle()
# tim2 = Turtle()
# tim3 = Turtle()

screen.setup(width=600, height=600)
screen.bgcolor("black") # set screen background color
screen.title("My snake game") # set title of screen
screen.tracer(0)# .tracer is an animation control to make your snake to be the same object not piece by piece. Set .tracy is 0 to turn it off.


# y_position = [0, -20, -40] # Our square is 20x20 and we want to move to the next one on the left side and lining side by side

# Solution 1
# list_object = [tim, tim2, tim3]
#
# for i in range(3):
#     list_object[i].color("white")
#     list_object[i].shape("square")
#     list_object[i].goto(x=y_position[i], y=0)


# How do we control the direction of snake

screen.listen()# Call the screen.listen() method to starting listening for keystrokes and the keystrokes are up, down, left and right.
screen.onkey(snake.up, "Up") #up is a method and snake.up is a function that will be triggered when the Up key is pressed.
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

# Move the snake
while game_is_on:
    screen.update()  # After you use screen.tracy(), you have to use screen.update() to update and refresh your screen. If you don't use it , the scrren won't show anything
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        # snake.head = self.segment[0] from snake.py
        #distance attribute compares distance from snake.head to food. 15 is from food size shape 10x10. We set it bigger to easier to detect.

        food.refresh() #After the snake hit the food, call method refresh to random the new location of food.
        scoreboard.increase_score()


    # Detect collision with wall. It means game over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False #To stop the while loop, end the movemnet and end the game.
        scoreboard.game_over()


    #Detect collision with tail. if head collides with any segment in the tail, it will trigger game over.
    for segment in snake.segment[1:]: #it means we will loop through all of this segmeng other that the first index(index 0).
        # We use slicing python snake.segment[1:]. It means count evey segment except index 0.

        if snake.head.distance(segment) < 10: #When head of snake (index:0) far from any segment list less than 10, game is over
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()