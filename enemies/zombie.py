# -*-coding: UTF-8 -*-
"""
Auther:Zhou Qinzhi
Date: 2020.12.02
"""
import pygame
import os
from .enemy import Enemy

imgs = []

for x in range(1, 19):
    num = str(x)
    if x < 10:
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/2", "3_enemies_1_run_00" + num + ".png")),
    (64, 64)))
    else:
        imgs.append(pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/enemies/2", "3_enemies_1_run_0" + num + ".png")),
            (64, 64)))


class Zombie(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "club"
        self.money = 30
        self.images = imgs[:]
        self.max_health = 9
        self.health = self.max_health