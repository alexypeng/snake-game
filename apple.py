from turtle import Turtle
from snake import Snake

class Apple():
    def __init__(self, snake):
        self.positions = []
        self.set_positions()

    def set_positions(self):
        for i in range(30):
            for j in range(30):
                self.positions.append((i*20, j*20))

    def generate_position(self, snake):
