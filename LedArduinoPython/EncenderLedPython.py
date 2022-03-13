import pyfirmata
 
port = "\\.\COM4" #Puerto COM de emulación en USB
pin = (13) #PIN donde va conectado el LED
 
#Conexión con placa Arduino
print("Conectando con Arduino por USB...")
tarjeta = pyfirmata.Arduino(port)
print("Conectado a Arduino por USB...")
while True:
    print("Encendiendo LED...")
    tarjeta.digital[pin].write(1)
    print("Encendido LED...")
    tarjeta.pass_time(3)
    print("Apagando LED...")
    tarjeta.digital[pin].write(0)
    print("Apagado LED...")
    tarjeta.pass_time(3)
tarjeta.exit()