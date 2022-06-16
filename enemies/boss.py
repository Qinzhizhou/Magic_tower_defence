# -*-coding: UTF-8 -*-
"""
Auther:Zhou Qinzhi
Date: 2020.12.08
"""
import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/10", "10_enemies_1_run_0" + add_str + ".png")),
       (150, 100)))

for x in range(1, 19):
    num = str(x)
    if x < 10:
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/10", "10_enemies_1_run_00" + num + ".png")),
    (150, 100)))
    else:
        imgs.append(pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/enemies/10", "10_enemies_1_run_0" + num + ".png")),
            (150, 100)))
# the contious 001 - 019 will be animation with animation count + = 1

class Boss(Enemy):

    def __init__(self):
        super().__init__() # make it to subclass as Enemy and inheritance the attribute
        self.name = "Boss"
        self.money = 500
        self.images = imgs[:]
        self.max_health = 100
        self.health = self.max_health