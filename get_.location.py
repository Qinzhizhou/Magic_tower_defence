# -*-coding: UTF-8 -*-
"""
Auther:Zhou Qinzhi
Date: 2020.11.30
"""
import pygame
import os

pygame.init()

class Game:
    def __init__(self):
        self.width = 1200
        self.height = 615#786
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.bg = pygame.image.load(os.path.join("game_assets","background_final.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        pygame.display.flip()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks) # 检查位置/路径的功能， 会print出来

            self.draw()

    pygame.quit()# 程序运行主界面

    def draw(self):
        self.screen.blit(self.bg, (0,0))
        for p in self.clicks:
            pygame.draw.circle(self.screen, (255, 0, 0), (p[0], p[1]), 5, 0)
        pygame.display.update()




game = Game()
game.run()