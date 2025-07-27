from pynput import keyboard
import threading
import traceback
from events import Event

def start_listener(event_queue):
    """
    Listen globally for Ctrl+C (press-and-release) and enqueue an Event.
    Runs in its own thread.
    """
    ctrl_pressed = False

    def on_press(key):
        # print(f"Key pressed: {key}")
        nonlocal ctrl_pressed
        if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            # print("Ctrl key pressed")
            ctrl_pressed = True

    def on_release(key):
        # print(f"Key released: {key}")
        nonlocal ctrl_pressed
        try:
            # If it's ‘c’ and Ctrl is down → fire
            if key.char == 'c' and ctrl_pressed:
                print("Ctrl+C detected")
                print("Enqueuing CTRL_C_PRESSED event",event_queue)
                event_queue.put_nowait(Event.CTRL_C_PRESSED)
                print("Enqueued CTRL_C_PRESSED event",event_queue)
        except AttributeError:
            # special keys: detect release of Ctrl
            if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
                ctrl_pressed = False

    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception:
        print("❗ pynput listener failed—check X server permissions:\n",
              traceback.format_exc())
