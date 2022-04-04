from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car = random.randint(0, 8)
        if random_car == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            starting_point = random.randint(-170, 170)
            new_car.goto(300, starting_point)
            self.cars.append(new_car)


    # def generate_cars(self):


    def move(self):
        for car in self.cars:
            car.backward(self.cars_speed)

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT






