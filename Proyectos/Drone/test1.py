import tkinter as tk
from djitellopy import Tello
from time import sleep
drone = Tello()

ventana = tk.Tk()
ventana.title("Drone Control")
ventana.geometry("300x300")


def actualizar_bateria():
    bateria["text"] = drone.get_battery()


bateria = tk.Label(ventana, bg="red", font="Helvetica 20")
actualizar_contador_bateria = tk.Button(ventana, text="Actualizar Bateria", command=actualizar_bateria)
conectar_drone = tk.Button(ventana, text="Conectar Drone", command=drone.connect)
despegue = tk.Button(ventana, text="Despegar", padx=30, pady=40, command=drone.takeoff)
aterrizaje = tk.Button(ventana, text="Aterrizar", padx=30, pady=40, command=drone.land)

bateria.grid(row=0, column=2)
actualizar_contador_bateria.grid(row=0, column=3)
conectar_drone.grid(row=1, column=2)
despegue.grid(row=2, column=1)
aterrizaje.grid(row=2, column=3)

ventana.mainloop()
