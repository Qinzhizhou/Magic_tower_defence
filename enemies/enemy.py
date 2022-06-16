# -*-coding: UTF-8 -*-
"""
Auther:Zhou Qinzhi
Date: 2020.11.29
"""
import math
import pygame
import os


class Enemy:


    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.path = [(19, 468), (68, 468), (114, 460), (154, 429), (176, 361), (187, 312), (231, 281), (296, 264), (345, 249), (366, 201), (373, 153), (395, 113), (433, 87), (469, 76), (509, 77), (555, 76), (611, 75), (652, 73), (690, 63), (728, 55), (767, 65), (799, 80), (833, 80), (876, 80), (928, 89), (967, 123), (984, 173), (975, 219), (949, 248), (906, 259), (861, 274), (823, 306), (801, 347), (804, 390), (824, 427), (857, 451), (895, 465), (933, 472), (971, 501), (981, 554), (980, 591)]
        # The moving path, which is got by get_location.py
        self.vel = 10  # speed
        self.x = self.path[0][0]
        self.y = self.path[0][1] # used path to get position x and y in self path list
        self.imgs =[] # imgs of enemy is list
        self.path_pos = 0
        self.move_count = 0
        self.move_step_dis = 0
        self.max_health = 0
        # all zero to initialize, this will be assigned in the process of game

    def draw(self, win):
         # draw enemies
        self.img = self.images[self.animation_count]
         # call back each imgs of the list with animation count
        win.blit(self.img, (self.x - self.width / 2, self.y - self.height / 2)) # draw out
        self.draw_health_bar(win) # with heath bar




    def move(self):


        self.animation_count += 1
        if self.animation_count >= len(self.images):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos] # give x1\y1 value with the position in path
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos + 1] # next point x2 y2

        dirn = ((x2 - x1) * 2, (y2 - y1) * 2) # used those 2 points to get direction
        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2) # distance of 2 points
        dirn = (dirn[0] / length, dirn[1] / length)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1])) # delta x, y think of a triangle

        self.x = move_x
        self.y = move_y


        # Go to next point
        if dirn[0] >= 0:  # moving right / direction
            if dirn[1] >= 0:  # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:  # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1

    """
       This idea is inspired by "Teach with tim" : https://github.com/techwithtim/Tower-Defense-Game/blob/master/enemies/enemy.py
       """
    def die (self, damage):

        self.health -= damage
        if self.health <= 0:
            return True
        return False


    def draw_health_bar(self, win):

        length = 50
        loseHP = length / self.max_health
        health_bar = loseHP * self.health

        pygame.draw.rect(win, (255,0,0), (self.x-30, self.y-75, length, 10), 0) # Red Lose HP
        pygame.draw.rect(win, (0, 255, 0), (self.x-30, self.y - 75, health_bar, 10), 0) # Green remains HP