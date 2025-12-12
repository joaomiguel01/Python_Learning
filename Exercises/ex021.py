import pygame

pygame.mixer.init()
music = pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass