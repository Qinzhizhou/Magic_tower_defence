#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:03:14 2020

@author: apple
"""

import pygame
from towers.tower import Tower
import os
import math
import time



menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")), (120, 70))

tower_imgs1 = []
archer_imgs1 = []
# load archer tower images, also make animation as enemy does.
for x in range(7,10):
    tower_imgs1.append\
        (pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/archer_towers/archer_1", str(x) + ".png")),
        (90, 90)))

# load archer images, the man on the tower
for x in range(38,50): #cloth
    archer_imgs1.append(
            pygame.image.load(os.path.join("game_assets/archer_towers/archer_top", str(x) + ".png")))


class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.tower_imgs = tower_imgs1[:]
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.range = 150   # Attack range
        self.original_range = self.range # Orign , because this can be bufferred
        self.inRange = False    # bull in range or not
        self.left = True # For filliping
        self.timer = time.time()
        self.damage = 1
        self.original_damage = self.damage
        self.moving = False # When put it down False, when loading True, can move with mouse
        self.name = "archer"

    def draw(self,win):
        super().draw_radius(win)
        super().draw(win)

        if self.inRange and not self.moving: # W
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 10] #
        
        if self.left == True: #
            add = -25
        else:
            add = -archer.get_width() + 10
        win.blit(archer, ((self.x + add), (self.y - archer.get_height() - 25)))

    def change_range(self,r): # used when support tower to give buff

        self.range = r
        

    def attack(self,enemies):

        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            
            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)  #distance  
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.die(self.damage) == True:
                    money = first_enemy.money
                    enemies.remove(first_enemy)
            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)


                    
        return money




tower_imgs = []
archer_imgs = []
# load archer tower images
for x in range(8,10):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/archer_towers/archer_1", str(x) + ".png")),
        (90, 90)))

# load archer images
for x in range(51,63): #armor
    archer_imgs.append(
            pygame.image.load(os.path.join("game_assets/archer_towers/archer_top", str(x) + ".png")))
  
class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 120
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1.5
        self.original_damage = self.damage
        
       

        #self.menu = Menu(self, self.x, self.y, menu_bg, [2500, 5500, "MAX"])
        #self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "archer2"

      
        
            
        
        
        
            
            
            
        
