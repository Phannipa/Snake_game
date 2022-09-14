from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


#Create scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 #Set initial score as 0
        self.color("white") #Must change font color to be white because the default of font color is black.
        self.hideturtle() #To hide the turtle object (arrow sign)
        self.penup() # Remove drawing line
        self.goto(0, 270)# Move from center of screen (align) to the top of screen
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT) # align means center of the screen


    def increase_score(self):
        self.score = self.score+1
        self.clear() #If we don't use clear method, it will overwrite the score.
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0) # To move game over word to the center of the scrren but we still see the score on the top of scree.
        self.write("Game over", False, align=ALIGNMENT, font=FONT)




