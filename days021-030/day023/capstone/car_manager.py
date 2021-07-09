from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__('square')
        self.color(choice(COLORS))
        self.pu()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(300, randint(-250, 250))

    def is_collision(self, player):
        return self.distance(player) < 15


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.cars.append(Car())

    def move_cars(self):
        for_removal = []
        for idx, car in enumerate(self.cars):
            car.bk(self.move_distance)
            if car.xcor() < -320:
                for_removal.append(idx)

        for i in sorted(for_removal, reverse=True):
            del self.cars[i]

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

    def is_collision(self, player):
        for car in self.cars:
            if car.is_collision(player):
                return True
        return False

    def game_over(self):
        for car in self.cars:
            car.ht()
