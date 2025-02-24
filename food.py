from turtle import Turtle
import turtle
import random

turtle.colormode(255)
shapes = ["turtle", "circle", "square", "triangle"]

# FOOD_COLORS = ["red", "green", "orange", "pink", "yellow", "purple"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_random_shapes()
        self.pu()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.food_random_colors()
        self.speed(0)
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

    def food_random_colors(self):
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        self.color((r, g, b))

    def food_random_shapes(self):
        self.shape(random.choice(shapes))
