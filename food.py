import random
from turtle import Turtle


class Food(Turtle):
    """
    This class depicts the food the snake will be chasing throughout the game and its actions.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        # Don't leave lines between movements
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        # Go very fast between point to give perception of reappearing
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move to a new random spot"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
