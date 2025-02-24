import random
from turtle import Turtle, Screen

STARTING_POSITIONS =  [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

BODY_COLORS = ["azure1", "chartreuse"]

class Snake:
    def __init__(self):
        self.screen = Screen()
        self.screen.register_shape("snake_head", (
            (-10, 0), (-5, 10), (0, 12), (5, 10), (10, 0), (5, -10), (0, -12), (-5, -10), (-10, 0)
        ))
        self.screen.register_shape("snake_body", (
            (-10, -5), (-8, 5), (8, 5), (10, -5), (8, -10), (-8, -10), (-10, -5)
        ))
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i, position in enumerate(STARTING_POSITIONS):
            self.add_segment(position, i)

    def add_segment(self, position, i):
        if i == 0:
            new_segment = Turtle()
            new_segment.shape("snake_head")
            new_segment.color("white")
        else:
            new_segment = Turtle()
            new_segment.shape("snake_body")
            new_segment.color(random.choice(BODY_COLORS))
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position(), None)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
