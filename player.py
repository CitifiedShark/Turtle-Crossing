from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.player = Turtle(shape="turtle")
        self.player.color("black")
        self.player.setheading(90)
        self.player.penup()
        self.player.teleport(0, -300)

    def move(self):
        self.player.forward(MOVE_DISTANCE)

    def next_level(self):
        self.player.teleport(0, -300)


