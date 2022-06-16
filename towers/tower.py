#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:03:16 2020

@author: apple
"""
import pygame
from menu.menu import Menu
import os
import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")), (200, 50))


class Tower:
    
    "abstract class for towers"

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 0     
        self.height = 0
        self.sell_price = [0,0,0]    #需要花费的价钱
        self.price = [0, 0, 0]
        self.level = 1  #可以升级
        self.selected = False

        self.tower_imgs = []
        self.damage = 1

        # define menu and buttons
        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, "MAX"])
        # self.menu.add_btn(upgrade_btn, "Upgrade")
        self.place_color = (0, 0, 255, 100)

        
      
    def draw(self,win):
        """
        draw the tower
        win: surface
        retrurn: none 
        """
        img = self.tower_imgs[self.level-1]
        win.blit(img,(self.x-img.get_width()/2,self.y-img.get_height()/2))  #确定显示图片的位置




#点击显示透明找(不知道有没有用，先把防护罩透明再看）


    def draw_radius(self, win):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self,win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self,X,Y):
        """
        returns if tower has been clocked on
        and selects tower if it was clickes
        x:init,y:init,reutrn:bool
        """

        img = self.tower_imgs[self.level-1]
        if X - img.get_width()//2<= self.x + self.width and X >= self.x:
            if Y - img.get_height()//2 <= self.y +self.height and Y>= self.y:
                return True
        return False

    
    
    
    def sell(self):
        """
        call to sell the tower, returns sell price
        """
        return self.sell_price[self.level-1]    #买出塔降一级
    
    
    
    def upgrade(self):
        """
        upgrades the tower for a given cost
        
        """
        if self.level < len(self.tower_imgs):
            self.level += 1
            self.damage += 1
    
    def get_upgrade_cost(self):
        """
        return the upgrade cost, if 0 then cannot upgrade anymore
        
        """
        return self.price[self.level-1]
        
    
    
    
    def move(self,x,y):  #这个最难
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y   #后加的

        
    def collide(self,otherTower):
        x2 = otherTower.x
        y2 = otherTower.y
        
        dis = math.sqrt((x2 - self.x)**2 + (y2 -self.y)**2)
        if dis>= 100:
            return False
        else:
            return True
    