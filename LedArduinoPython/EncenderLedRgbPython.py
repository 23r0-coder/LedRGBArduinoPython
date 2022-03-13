from pyfirmata import Arduino, PWM
import random #libreria para numeros random
board = Arduino("\\.\COM4") #conexion entre la placa y Python

#pins donde se coloca el led RGB en la placa (Arduino)
rojo= 9
verde = 10
azul = 11

#establece las variables como modulables
board.digital[rojo].mode = PWM
board.digital[azul].mode = PWM
board.digital[verde].mode = PWM

#manda numeros random del 0 al 255 para los colores y da un delay de 0.5 segs y se ejecuta hasta que se desconecte.
while True:
   board.digital[rojo].write(random.random())
   board.digital[azul].write(random.random())
   board.digital[verde].write(random.random())
   board.pass_time(0.5)
