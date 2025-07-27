from pynput import keyboard
from events import Event

def start_listener(event_queue, loop):
    ctrl_pressed = False

    def on_press(key):
        nonlocal ctrl_pressed
        if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            ctrl_pressed = True

    def on_release(key):
        nonlocal ctrl_pressed
        try:
            if key.char == 'c' and ctrl_pressed:
                loop.call_soon_threadsafe(event_queue.put_nowait, Event.CLIPBOARD_TRIGGER)
        except AttributeError:
            if key == keyboard.Key.esc:
                loop.call_soon_threadsafe(event_queue.put_nowait, Event.STOP)
            elif key == keyboard.Key.space:
                loop.call_soon_threadsafe(event_queue.put_nowait, Event.TOGGLE_PAUSE)

        if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            ctrl_pressed = False

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
