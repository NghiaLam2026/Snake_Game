from turtle import Turtle
ALIGHTMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGHTMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGHTMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updated_scoreboard()
        
