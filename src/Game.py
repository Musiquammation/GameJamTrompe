from __future__ import annotations
import pygame
from pygame import Surface
from Player import Player
from InputHandler import InputHandler

class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 450
        self.player = Player(0, 0, [])
        self.inputHandler = InputHandler()
        self.frameCount = 0
        self.camera_offset = pygame.Vector2(0, 0)

    def update(self):
        self.player.update(self)
        
        self.camera_offset.x += (self.player.x - self.camera_offset.x) * 0.1
        self.camera_offset.y += (self.player.y - self.camera_offset.y) * 0.1
        
        self.frameCount += 1

    def draw(self, screen: Surface):
        screen.fill((0, 0, 0))
        
        self.player.draw(screen, self.camera_offset)