from turtle import Turtle

# Set movement speed
MOVE_DISTANCE = 20

# Angle to direction translation, starting 0 angle at right and going upwards
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    """
    This class depicts the snake and its actions.
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        # Pointer showing the head of the snake
        self.head = self.segments[0]

    def create_snake(self):
        """Create new snake parts and place them on the canvas"""
        for i in range(3):
            self.add_segment((- i * 20, 0))

    def move(self):
        """Move all segments starting from the head, with the rest segments following"""
        segments = self.segments
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Point snake upwards, if applicable"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Point snake downwards, if applicable"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Point snake leftwards, if applicable"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Point snake rightwards, if applicable"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        """Add new snake segment at the given position

        Parameters
        ----------
        position : tuple(float,float)
            An (x,y) position in the canvas

        """
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        """Add new segment at the end of the snake"""
        self.add_segment(self.segments[-1].position())

    def restart(self):
        """Reset the snake"""
        # Move all segments to the start
        for segment in self.segments:
            segment.goto(1000, 1000)
        # Remove previous snake
        self.segments.clear()
        # Create new snake
        self.create_snake()
        # Make head pointer point to the new head of the snake
        self.head = self.segments[0]