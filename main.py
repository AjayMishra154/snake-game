import time
from turtle import Screen
import snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
food = Food()
score = Score()
new_snake = snake.Snake()

screen.onkey(fun=new_snake.up, key="Up")
screen.onkey(fun=new_snake.down, key="Down")
screen.onkey(fun=new_snake.right, key="Right")
screen.onkey(fun=new_snake.left, key="Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    if new_snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        new_snake.extend()
        score.score_refresh()
    if new_snake.head.xcor() < -280 or new_snake.head.xcor() > 280 or new_snake.head.ycor() < -280 or new_snake.head.ycor() > 280:

        score.refresh()
        new_snake.refresh()

    for segments in new_snake.segments:
        if segments == new_snake.head:
            pass
        elif new_snake.head.distance(segments) < 10:
            score.score_refresh()
            new_snake.refresh()

screen.exitonclick()
