import threading
import time
import random
from threading import Lock

global contador
contador = 0

def realizar_tarea(nombre, tiempo):

    with lock:
        contador += 1
        print(f"{nombre} ha comenzado. Hay un total de {contador} procesos ahora mismo.")
        time.sleep(tiempo)
        print(f"{nombre} ha terminado. Hay un total de {contador} procesos ahora mismo.")
        contador -= 1

tareas = [("Lavar platos", random.randint(1, 9)),
          ("Barrer", random.randint(1, 9)),
          ("Lavar ropa", random.randint(1, 9)),
          ("Cocinar", random.randint(1, 9))]

lock = Lock()
hilos=[]

for tarea, tiempo in tareas:
    hilo = threading.Thread(target= realizar_tarea, args=(tarea, tiempo))
    hilo.start()
    hilos.append(hilo)
    #hilo.join()

for hilo in hilos:
    hilo.join()