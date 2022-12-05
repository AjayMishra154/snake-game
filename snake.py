from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_position:
            new_segment = Turtle("circle")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            num_x = self.segments[seg_num - 1].xcor()
            num_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(num_x, num_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def extend(self):
        new_segment = Turtle(shape="circle")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.color("white")
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def refresh(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()

        self.create_snake()
        self.head = self.segments[0]