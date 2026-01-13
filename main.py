import pygame as pg

#inicializar todos los modulos de pygame
pg.init()

#crear pantallas o sourceface
pg.display.set_mode((800,600))#definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame")#Agrega un titulo en string a mi ventana

game_over = True

while game_over:
    for events in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(events)
        if events.type == pg.QUIT:
            game_over = False


            
#cierre de pantalla
pg.quit()