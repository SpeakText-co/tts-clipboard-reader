import tkinter as tk
import asyncio
class ControlUI:
    def __init__(self, app):
        self.app = app
        self.root = tk.Tk()
        self.root.title("TTS Clipboard Reader")
        self.root.geometry("300x200")
        self.root.configure(bg="white")

        tk.Button(self.root, text="Speak Clipboard", command=self.safe(app.speak_clipboard)).pack(pady=10)
        tk.Button(self.root, text="Stop", command=self.safe(app.stop)).pack()
        tk.Button(self.root, text="Pause", command=self.safe(app.pause)).pack()
        tk.Button(self.root, text="Resume", command=self.safe(app.resume)).pack()

        self.label = tk.Label(self.root, text="Status: idle", bg="white")
        self.label.pack(pady=20)

    def safe(self, coro_func):
        def wrapper():
            asyncio.run_coroutine_threadsafe(coro_func(), self.app.loop)
        return wrapper

    def set_status(self, text):
        self.label.config(text=f"Status: {text}")

    def run(self):
        self.root.mainloop()
