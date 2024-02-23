
import pygame
from random import randint
# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((640 ,480)) #Se cre la ventana del juego
pygame.display.set_caption("Ejemplo 1") 
fuente = pygame.font.Font(None, 70) #Se establede la fuente y el tamaño del texto
# Crea el objeto pelota
ball = pygame.image.load('pelota.png')  #Se crea la pelota mediante una imagen
speed = [randint(3,6),randint(3,6)]


# Obtengo el rectángulo del objeto anterior
ballrect = ball.get_rect() #Se crea la hitbox de la pelota

# Inicializo los valores con los que se van a mover la pelota
speed = [4,4]

# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)
# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("plataforma.png")
baterect = bate.get_rect()

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240,450)
# crea el objeto ladrillo
ladrillo = pygame.image.load('slakoth.jpg')


class ladrillo(pygame.sprite):
    def __init__(self, x, y, puntos):
     self.x = x
     self.y = y
     self.puntos = puntos
     self.rect = pygame.Rect(self.x, self.y, self.puntos)

    def update(self):
       pygame.draw.rectself.rect
    
    

# Bucle principal del juego
jugando = True
while jugando:
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
     # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-6,0) #Se establece la tecla izquierda para que el bate se mueve a la izquierda
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(6,0) #Se establece la tecla derecha para que el bate se mueva a la derecha
    
    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    # Muevo la pelota
    ballrect = ballrect.move(speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
        

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    if keys[pygame.K_LEFT] and baterect.left < 0:
        baterect = baterect.move(6,0)
    if keys[pygame.K_RIGHT] and baterect.right > ventana.get_width():
        baterect = baterect.move(-6,0)
    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (0, 0, 255)) #Añade el texto de GAME OVER cuando se pierde
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2 #Establec
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
        speed[1] =- speed[1]

    else:
        ventana.fill((252, 243, 207))
       # Dibujo la pelota
        ventana.blit(ball, ballrect)

    # Dibujo el bate
        ventana.blit(bate, baterect)

    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()