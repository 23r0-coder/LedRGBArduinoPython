from pyfirmata import Arduino, PWM
import random
board = Arduino("\\.\COM4")

rojo= 9
verde = 10
azul = 11

board.digital[rojo].mode = PWM
board.digital[azul].mode = PWM
board.digital[verde].mode = PWM

while True:
   board.digital[rojo].write(random.random())
   board.digital[azul].write(random.random())
   board.digital[verde].write(random.random())
   board.pass_time(0.5)