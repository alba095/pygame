import pygame as pg

#inicializar todos los modulos de pygame
pg.init()

#crear pantallas o sourceface
pantalla= pg.display.set_mode((800,600))#definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame")#Agrega un titulo en string a mi ventana

game_over = True
x=0
vx= 1
while game_over:
    for events in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(events)
        if events.type == pg.QUIT:
            game_over = False

    pantalla.fill((112, 95, 232))#asignar el color de pantalla en RGB


    x = x + vx
    if x==0 or x==800:
        vx=vx*-1
    #agregamos objetos a la pantalla
    #draw.rect(surface,color en (rgb),posiciones(posicionx,posiciony,tamañoX,tamañoY)
    pg.draw.rect(pantalla,(22, 22, 28),(x,300-15,30,30))#le restamos 15 para que este en el centro, le restamos la mitad de 30 que es lo que mide cada lado



    pg.display.flip()#Funcion para recargar toda la configuracion que va en la pantalla

#cierre de pantalla
pg.quit()