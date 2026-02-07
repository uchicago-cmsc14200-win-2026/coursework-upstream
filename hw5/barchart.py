"""
CMSC 14200, Winter 2026
Homework 5
"""

import pygame
import sys

class BarChart():

    def __init__(self, data: list):
        self.current_data = list(data) # make a copy
        self.target_data  = list(data) # make a copy
        self.animation_speed = 0.1

    def set_target_data(self, new_data: list) -> None:
        self.target_data = list(new_data) # make a copy
        for i in range(len(self.target_data)):
            self.current_data[i]['NOC'] = self.target_data[i]['NOC']

    def update(self) -> None:
        """
        Perform the calculations necessary to animate current_data toward
        target_data.
        """
        deco = "Decorated_Athletes"
        for i in range(len(self.current_data)):
            diff = self.target_data[i][deco] - self.current_data[i][deco]
            self.current_data[i][deco] += diff * self.animation_speed

            if abs(diff) < 0.01:
                self.current_data[i] = self.target_data[i]
