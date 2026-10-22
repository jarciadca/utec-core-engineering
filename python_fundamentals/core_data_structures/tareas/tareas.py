#!/usr/bin/env python3

tareas = []

#try:
#    with open("tareas.txt", "r")

#except FileNotFoundError:
#    print("No existe en archivo solicitado")

while True:
    tarea = input("Entrar tarea:")

    if not tarea:

        break
    tareas.append(tarea)

for i in range(0, len(tareas)):
    j = i + 1
    print(f"{j}- {tareas[i]}")

tarea_completa = input("Entrar número de tarea completada:")

try
    isinstance(tarea_completa, int):



tareas.remove(tarea_completa - 1)
    
