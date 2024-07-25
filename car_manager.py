import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars = []

    def spawn_car(self):
        if len(self.cars) < 40:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=None, stretch_len=2)
            color = random.choice(COLORS)
            car.color(color)
            random_y = random.randint(-260, 300)
            random_x = random.randint(340, 940)
            car.teleport(random_x, random_y)
            car.setheading(180)

            self.cars.append(car)

        self.distance = STARTING_MOVE_DISTANCE

    def move_car(self):
        for car in self.cars:
            car.forward(self.distance)

            if car.xcor() < -340:
                car.hideturtle()
                self.cars.remove(car)

    def next_level(self):
        self.distance += MOVE_INCREMENT
