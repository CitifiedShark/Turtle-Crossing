from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.score = 0
        self.level_value = 1

        self.level = Turtle()
        self.level.hideturtle()
        self.level.teleport(-250, 275)
        self.level.write(f"level: {self.level_value}", move=False, align="center", font=('monospace', 12, 'normal'))

    def next_level(self):
        self.level_value += 1
        self.level.clear()
        self.level.write(f"level: {self.level_value}", move=False, align="center", font=('monospace', 12, 'normal'))
