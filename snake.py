from turtle import Turtle

MOVE_DISTANCE = 20


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.up()
            new_segment.color("white")
            new_segment.goto(0 - i * 20, 0)
            self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def check_collision(self):
        if self.head.xcor() > 280 or self.head.xcor() < -300 or self.head.ycor() > 280 or self.head.ycor() < -300:
            return True

        for i in range(1, len(self.segments)):
            if self.segments[i].pos() == self.head.pos():
                return True

        return False
