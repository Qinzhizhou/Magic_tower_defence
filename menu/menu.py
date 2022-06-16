# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 06:33:41 2020

@author: junemurphy
"""


import pygame
import os

pygame.font.init()

star = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "star.png")),(20,20))


class Button:
    def __init__(self, menu, img, name):
        self.name = name
        self.img = img
        self.x = menu.x
        self.y = menu.y
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):

        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >=self.y:
                return True
            return False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class PlayPauseButton(Button):
    def __init__(self, play_img, pause_img, x, y):
        self.img = play_img
        self.play = play_img
        self.pause = pause_img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.paused = True

    def draw(self, win):
        if self.paused:
            win.blit(self.play, (self.x, self.y))
        else:
            win.blit(self.pause, (self.x, self.y))

class VerticalButton(Button):
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost


class Menu:

    def __init__ (self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_names= []
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.tower = tower
        
    def get_clicked(self,X,Y):

        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name

        return None


class VerticalMenu(Menu):

    def __init__(self, x, y, img):
        
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("impact", 25)
        #The menu

    def add_btn(self, img, name, cost):

        self.items += 1
        btn_x = self.x - 70
        btn_y = self.y - 133 + (self.items -1 ) * 110
        self.buttons.append(VerticalButton(btn_x, btn_y, img, name, cost))
        # Buy button

    def get_item_cost(self, name):
        # Buy something pay some money
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def draw(self, win):
        # draw Vertical menu
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x + 35, item.y + item.height - 25)) # Draw money imgaes with amount
            text = self.font.render(str(item.cost), 1, (255, 255, 255))
            win.blit(text, (item.x + item.width/2 - text.get_width()/2 + 10, item.y + item.height - 30))