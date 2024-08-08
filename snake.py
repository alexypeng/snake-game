from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]


class Snake:
    """Class that creates the snake in the Snake Game."""
    def __init__(self):
        """Initializes the snake and defines the variables."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake at the beginning of the game."""
        for position in STARTING_POSITIONS:
            self.grow(position)

    def up(self):
        """Turns the snake up."""
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Turns the snake down."""
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)

    def left(self):
        """Turns the snake left."""
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(180)

    def right(self):
        """Turns the snake right."""
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        """Moves the snake forward."""
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def check_collision(self):
        """Checks if the snake has collided with the wall or itself."""
        if self.head.xcor() > 280 or self.head.xcor() < -300 or self.head.ycor() > 300 or self.head.ycor() < -280:
            return True

        for segment in self.segments[1:]:
            if segment.distance(self.head) < 10:
                return True

        return False

    def grow(self, pos):
        """Creates a new segment and adds it to the snake."""
        new_segment = Turtle(shape="square")
        new_segment.up()
        new_segment.color("white")
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the end of the snake."""
        self.grow(self.segments[-1].position())
