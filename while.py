i = 0
while i <= 10:
    print(i)
    if i == 5:
        break #rompe el bucle
        
    i += 1
    
x = 0
print("Hola mundo")
while x <= 10:
    x += 1
    if x == 5:
        continue # salta las instruciones inmediata q viene debajo del continue, y por eso no imprime el 5
    print(x)
    
print("Hola mundo")
#Se define el puntaje de vida inicial.
import random

life_player1 = 200

#Bucle while confirma vida del jugador.
while life_player1 > 0:
  # La f viene de format (f-string o cadena de formato). Sirve para crear cadenas de texto 
  # donde puedes incrustar variables directamente sin tener que andar uniendo textos con 
  # comas o signos de más (+).
  print(f"Tus puntos de vida son {life_player1}")
  #Con random se puede definir el daño del adversario.
  life_player1 -= random.randint(1,30)

#Al salir del bucle significa que el jugador se quedó sin puntos de vida.
print("GAME OVER.")