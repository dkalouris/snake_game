from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    """Class that keeps track of the current score and also previous highscore."""

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0, 260)
        self.score = 0
        self.highscore = self.get_prev_highscore()
        self.update_scoreboard()

    def get_prev_highscore(self):
        """Read 'data.txt' file and get previous highscore"""
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def write_new_highscore(self):
        """If scored higher that previous highscore, write new highscore to 'data.txt'"""
        if self.score > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.highscore = self.score

    def update_scoreboard(self):
        """Show the current score and highscore to the screen"""
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def score_point(self):
        """Increase score and show the current score and highscore to the screen"""
        self.score += 1
        self.update_scoreboard()

    def restart(self):
        """Write new highscore if applicable, and reset scoreboard"""
        self.write_new_highscore()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)