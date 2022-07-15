import threading
import os
import winsound
import time

def funcion(numero):
    for n in range(10):
        valor=n*n+n
        print(valor,"--->",numero)
        winsound.Beep(2500,100)

if __name__ == '__main__':
    hilos = []

    cores = os.cpu_count()
    print("Tienes ", cores, " cores")

    print("----- Instanciar")
    for n in range(cores):
        hilo = threading.Thread(target=funcion, args=(n,))
        hilos.append(hilo)

    print("----- Ejecutar")
    for hilo in hilos:
        hilo.start()

    print("----- Espera")
    for hilo in hilos:
        hilo.join()

    print("----- Regreso a la ejecucion inicial")

    time.sleep(10)