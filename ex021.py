#Faça um programa que abra e reproduza o áudio de um arquivo MP3.
'''
#Minha Resolução
import playsound
playsound.playsound('sample.mp3')
'''

#Resolução Guanabara
import pygame

#para inicar a bibliteca do pygame
pygame.init()

pygame.mixer.music.load('sample.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()