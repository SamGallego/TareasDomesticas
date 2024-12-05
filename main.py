import threading
import time
import random

# Función para simular una tarea
def realizar_tarea(nombre, tiempo):
    print(f"{nombre} ha comenzado.")
    time.sleep(tiempo)
    print(f"{nombre} ha terminado.")

# Lista de tareas
tareas = [("Lavar platos", random.randint(1, 5)),
          ("Barrer", random.randint(1, 5)),
          ("Lavar ropa", random.randint(1, 5)),
          ("Cocinar", random.randint(1, 5))]

lock = threading.Lock()

def tarea_con_lock(nombre, tiempo):
    with lock:
        realizar_tarea(nombre, tiempo)

print("\nEjemplo con Lock:")
hilos_lock = []

for tarea, tiempo in tareas:
    hilo = threading.Thread(target=tarea_con_lock, args=(tarea, tiempo))
    hilos_lock.append(hilo)
    hilo.start()

for hilo in hilos_lock:
    hilo.join()
