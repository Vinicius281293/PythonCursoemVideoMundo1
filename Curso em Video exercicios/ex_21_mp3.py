"""
Exercício Python 21:
Faça um programa
em Python que abra e reproduza o áudio de um arquivo MP3.

"""

# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.\n')
import pygame

pygame.init()
pygame.mixer.music.load('bonjovi.mp3')
pygame.mixer.music.play()
pygame.event.wait()
