# Exercício Python #021 - Tocando um MP3
import pygame
pygame.init()
pygame.mixer.music.load("exemplo.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
