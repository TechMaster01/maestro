import time
from pynput.keyboard import Listener as KeyboardListener, Controller as KeyboardController, Key
from threading import Thread, Event

# Variable configurable
intervalo_tiempo = 2.0  # Cambia este valor según tus necesidades

keyboard_controller = KeyboardController()
stop_event = Event()

def press_ctrl_loop():
    print(f"Presionando CTRL cada {intervalo_tiempo} segundos. (Presiona ESC para detener)")
    while not stop_event.is_set():
        keyboard_controller.press(Key.ctrl)
        keyboard_controller.release(Key.ctrl)
        time.sleep(intervalo_tiempo)
    print("Se detuvo el presionado automático de CTRL.")

def on_press(key):
    if key == Key.esc:
        print("Tecla ESC detectada, deteniendo...")
        stop_event.set()  # Señalamos que el hilo debe detenerse
        return False      # Detener el listener de teclado

# El hilo ya no será daemon, así Python espera hasta que termine
ctrl_thread = Thread(target=press_ctrl_loop)
ctrl_thread.start()

with KeyboardListener(on_press=on_press) as listener:
    listener.join()

ctrl_thread.join()  # Esperamos explícitamente que termine el hilo antes de salir