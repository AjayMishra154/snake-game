from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(-100, 270)
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(arg=f"Score :{self.score}   HighScore : {self.high_score}", align="left", font=("arial", 20, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align="center", font=("arial", 30, "normal"))

    def refresh(self):
        if self.score > self.high_score:

            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.score_refresh()
