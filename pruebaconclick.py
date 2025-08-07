import time
from pynput.keyboard import Listener as KeyboardListener, Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
from threading import Thread

# Variables configurables
intervalo_ctrl = 2.7  # intervalo para presionar CTRL
intervalo_click = 2.2  # intervalo para hacer click

keyboard_controller = KeyboardController()
mouse_controller = MouseController()
stop_flag = False

def press_ctrl_loop():
    global stop_flag
    print(f"Presionando CTRL cada {intervalo_ctrl} segundos. (Presiona ESC para detener)")
    while not stop_flag:
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.release(Key.ctrl)
        time.sleep(intervalo_ctrl)
    print("Se detuvo el presionado automático de CTRL.")

def click_loop():
    global stop_flag
    print(f"Haciendo click izquierdo cada {intervalo_click} segundos. (Presiona ESC para detener)")
    while not stop_flag:
        mouse_controller.click(Button.left, 1)
        time.sleep(intervalo_click)
    print("Se detuvo el click automático.")

def on_press(key):
    global stop_flag
    if key == Key.esc:
        stop_flag = True
        print("Tecla ESC detectada, deteniendo...")
        return False  # Detener el listener de teclado

# Iniciar hilos
ctrl_thread = Thread(target=press_ctrl_loop, daemon=True)
click_thread = Thread(target=click_loop, daemon=True)
ctrl_thread.start()
click_thread.start()

with KeyboardListener(on_press=on_press) as listener:
    listener.join()
