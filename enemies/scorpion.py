# -*-coding: UTF-8 -*-
"""
Auther:Zhou Qinzhi
Date: 2020.11.30
"""
import pygame
import os
from .enemy import Enemy

imgs = []

for x in range(1, 19):
    num = str(x)
    if x < 10:
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/1", "1_enemies_1_run_00" + num + ".png")),
    (64, 64)))
    else:
        imgs.append(pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/enemies/1", "1_enemies_1_run_0" + num + ".png")),
            (64, 64)))

class Scorpion(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "scorpion"
        self.money = 20
        self.max_health = 3
        self.health = self.max_health
        self.images = imgs[:]
