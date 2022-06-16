#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:02:02 2020

@author: apple
"""
import pygame
import os
from enemies.scorpion import Scorpion
from enemies.zombie import Zombie
from enemies.knight import Knight
from enemies.boss import Boss
from towers.archertower import ArcherTowerLong, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower
from menu.menu import VerticalMenu, PlayPauseButton
import time
import random
pygame.font.init() # Initialize the font module eg. lives、money、wave etc. About information shown on surface
pygame.init() # Initialize Pygame module


# Game resources used in this project
lives_img = pygame.image.load(os.path.join("game_assets", "heart.png"))
start_img = pygame.image.load(os.path.join("game_assets", "background_final.png"))
star_img = pygame.image.load(os.path.join("game_assets", "star.png"))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","side_menu_bg.png")), (100,450))
wave_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","wave_bg.png")), (225, 75))
buy_archer1 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu","archer1_icon.png")), (140,120))
buy_archer2 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu","archer2_icon.png")), (140,125))
buy_damage = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu", "damage_icon.png")), (140,120))
buy_range= pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu", "range_icon.png")), (140,120))
play_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu", "pause.png")), (80,80))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu", "pause2.png")), (80,80))
sound_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu", "music_on.png")), (80,80))
sound_btn_off = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu", "music_off.png")), (80,80))
attack_tower_names = ["archer","archer2"]
support_tower_names = ["range","damage"]
pygame.mixer.music.load(os.path.join("game_assets", "music.wav"))

"""
The game assets or game elements png files are mostly download on CRAFTPIX.NET. Qinzhi Zhou have purchased 2 packages of
sets "ARCHER TOWER GAME ASSETS" and "Magic Tower Game Assets ", which including tower and archer and some button imgs. 
Authority of download and used these assets in project is available. The map and other elements are designed by group 
member Tianshi Sun. 

Reference:
game assets resource: CRAFTPIX.net: url: https://craftpix.net/product/tower-defense-2d-game-kit/
list serve as an inspiration:
Tower denfense tutorial video: url: https://www.youtube.com/watch?v=iLHAKXQBOoA&list=PLzMcBGfZo4-nTARLniGMmigJT7P17wDDX
CSDN tower defense tutrial: url: https://blog.csdn.net/qq_41620823/article/details/103741989


"""
waves = [[1, 0, 0, 0],  # 0
        [20, 0, 0],  # 1
        [50, 0, 0],  # 2
        [100, 0, 0],  # 3
        [0, 20, 0],  # 4
        [0, 50, 1, 1],  # 5
        [0, 100, 0, 1],  # 6
        [20, 100, 5, 1],  # 7
        [50, 100, 5, 1],  # 8
        [100, 100, 5, 3],  # 9
        [0, 30, 50, 5],  # 10
        [0, 20, 100, 5],  # 11
        [0, 0, 0, 30],  # 13
        ]


class Game:
    def __init__(self,win):
        self.width = 1200
        self.height = 615
        self.win = win
        # pygame surface init

        self.lives = 10
        self.life_font = pygame.font.SysFont("impact", 30)
        self.money = 3000
        self.wave = 0
        # Game information

        self.enemies = []
        self.current_wave = waves[self.wave][:]
        self.attack_towers = []
        self.support_towers = []
        # Towers and enemies init

        self.bg = pygame.image.load(os.path.join("game_assets","background_final.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        # Background

        self.menu = VerticalMenu(self.width - side_img.get_width() + 35, 250, side_img)
        self.menu.add_btn(buy_archer1, "buy_archer1", 500)
        self.menu.add_btn(buy_archer2, "buy_archer2", 750)
        self.menu.add_btn(buy_range, "buy_range", 1000)
        self.menu.add_btn(buy_damage, "buy_damage", 1000)
        # Side menu object

        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, 10, self.height - 110)
        self.soundButton = PlayPauseButton(sound_btn, sound_btn_off, 100, self.height - 110)
        # Button

        self.moving = False
        self.moving_object = None
        # Click_moving object

        self.selected_tower = None
        self.music_on = True
        self.pause = True
        self.timer = time.time()
        # Others





    def get_waves_enemies(self):

      #  generate the next enemy or enemies to show

        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0: # at start/init  or when no enemies, then waves + 1
                self.wave += 1 # to next wave
                self.current_wave = waves[self.wave] # call back to waves we give, where contains information foe enemy
                self.pause = True # when no pause
                self.playPauseButton.paused = self.pause

        else:
            wave_enemies = [Scorpion(), Zombie(), Knight(), Boss()] # we make our four enemies in specific wave

            for x in range(len(self.current_wave)): # for each enemy in wave, loop
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])  # put wave enemies in list

                    self.current_wave[x] = self.current_wave[x] - 1 # go to next
                    break

    def run(self):
        pygame.mixer.music.play(loops = -1) # play musice
        run = True
        clock = pygame.time.Clock()

        while run: 
            clock.tick(500)

            if self.pause == False:
                # gen monsters
                if time.time() - self.timer >= random.randrange(1, 6)/2:
                    self.timer = time.time()
                    self.get_waves_enemies()
                
            pos = pygame.mouse.get_pos()
            if self.moving_object:
                self.moving_object.move(pos[0],pos[1])
                tower_list = self.attack_towers[:] + self.support_towers[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)

            #main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


                if event.type == pygame.MOUSEBUTTONDOWN:                    
                    if self.moving_object:#if you are moving an object and click
                        not_allowed = False
                        tower_list = self.attack_towers[:] + self.support_towers[:]

                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)

                        self.moving_object.moving = False
                        self.moving_object = None

                    else:
                        # check for play or pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            self.pause = not(self.pause)
                            self.playPauseButton.paused = self.pause

                        if self.soundButton.click(pos[0], pos[1]):
                            self.music_on = not(self.music_on)
                            self.soundButton.paused = self.music_on
                            if self.music_on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        #looking if you click on side menu
                        side_menu_button = self.menu.get_clicked(pos[0],pos[1])

                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_button)


                        #look if you clicked on attack tower or support tower
                        btn_clicked = None
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0],pos[1])

                        if not(btn_clicked):
                            for tw in self.attack_towers :
                                if tw.click(pos[0],pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False                                 
                  
                        #looking if you clicked on support tower
                            for tw in self.support_towers:
                                if tw.click(pos[0],pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False
                       

            # loop through enemies
            if not self.pause:
                to_del = []
                for en in self.enemies:
                    en.move()
                    if  en.y > 580:
                        to_del.append(en)
                        #delete all enemies reach the end point on the windows, the enemy will be remove.
                for d in to_del:
                    self.lives -= 1
                    self.enemies.remove(d)
                        # Enemies should remove will put in the list, for loop to remove them, at the same time
                        # You will lose 1HP when enemies finished his path.

                # loop through attack towers
                for tw in self.attack_towers:
                    self.money += tw.attack(self.enemies)
                    # enemies will be attacked by towers when they in range
                    # Kill an enemies will earn money

                # loop through
                for tw in self.support_towers:
                    tw.support(self.attack_towers)
                    # support towers give buff to attack towers



                # if you lose, end the game.
                if self.lives <= 0:
                    print("You Lose")
                    run = False

                # if you win, end the game.
                if self.wave >= 13:
                    print("You win")
                    run = False

            self.draw()
          


    def point_to_line(self, tower):
        return True




    def draw(self):
        self.win.blit(self.bg, (0, 0))
        
        # draw placement rings
        if self.moving_object:
            for tower in self.attack_towers:
                tower.draw_placement(self.win)



            for tower in self.support_towers:
                tower.draw_placement(self.win)

            self.moving_object.draw_placement(self.win)

        #draw enemies
        for en in self.enemies:
            en.draw(self.win)

        # draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)

        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)


        #redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(self.win)

        #drawing moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        #draw Verticalmenu
        self.menu.draw(self.win)

        #draw play pause button
        self.playPauseButton.draw(self.win)

        # draw music toggle button
        self.soundButton.draw(self.win)

        # draw lives
        text = self.life_font.render(str(self.lives), 1, (255, 255, 255))
        life = pygame.transform.scale(lives_img, (40, 40))
        start_x = self.width - life.get_width() - 35

        self.win.blit(text, (start_x - text.get_width() - 20, 10))
        self.win.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(star_img, (40, 40))
        start_x = self.width - life.get_width() - 35

        self.win.blit(text, (start_x - text.get_width() - 20, 70))
        self.win.blit(money, (start_x, 65))

        pygame.display.update()

        # draw wave
        self.win.blit(wave_bg, (10, 10))
        text = self.life_font.render("Wave #" + str(self.wave), 1, (255, 255, 255))
        self.win.blit(text, (10 + wave_bg.get_width() / 2 - text.get_width() / 2, 25))

        pygame.display.update()


    
    # Operation on side menu, but towers
    def add_tower(self, name):
        x, y = pygame.mouse.get_pos() # mouse to click get the x\y
        name_list = ["buy_archer1", "buy_archer2", "buy_damage", "buy_range"]
        object_list = [ArcherTowerLong(x,y),ArcherTowerShort(x,y),DamageTower(x,y),RangeTower(x,y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")
       




