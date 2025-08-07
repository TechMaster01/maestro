import time
from pynput.keyboard import Listener as KeyboardListener, Controller as KeyboardController, Key
from threading import Thread

# Variable configurable
intervalo_tiempo = 1.7  # Cambia este valor según tus necesidades

keyboard_controller = KeyboardController()
stop_flag = False

def press_ctrl_loop():
    global stop_flag
    print(f"Presionando CTRL cada {intervalo_tiempo} segundos. (Presiona ESC para detener)")
    while not stop_flag:
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.release(Key.ctrl)
        time.sleep(intervalo_tiempo)
    print("Se detuvo el presionado automático de CTRL.")

def on_press(key):
    global stop_flag
    if key == Key.esc:
        stop_flag = True
        print("Tecla ESC detectada, deteniendo...")
        return False  # Detener el listener de teclado

ctrl_thread = Thread(target=press_ctrl_loop, daemon=True)
ctrl_thread.start()

with KeyboardListener(on_press=on_press) as listener:
    listener.join()
