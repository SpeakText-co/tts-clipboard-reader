import asyncio
import threading
import tkinter as tk
from events import Event

class Overlay:
    def __init__(self):
        self.root = None

    def show(self):
        # Must run in main thread; so we schedule via call_soon_threadsafe
        if self.root is not None:
            return
        self.root = tk.Tk()
        self.root.attributes('-topmost', True, '-fullscreen', True, '-alpha', 0.3)
        self.root.configure(bg='black')
        tk.Label(self.root, text="Speaking…", fg="white", bg="black", font=("Arial", 48)).pack(expand=True)
        # auto‑destroy after 2s
        self.root.after(2000, self.root.destroy)
        self.root.mainloop()
        self.root = None

    async def handle_event(self, event, loop):
        if event is Event.SHOW_OVERLAY:
            # run blocking tkinter in executor
            await loop.run_in_executor(None, self.show)
