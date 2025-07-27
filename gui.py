import tkinter as tk
import asyncio
class ControlUI:
    def __init__(self, app):
        self.app = app
        self.root = tk.Tk()
        self.root.title("TTS Clipboard Reader")
        self.root.geometry("350x400")
        self.root.configure(bg="white")

        tk.Label(self.root, text="Voice (e.g. en, en-gb):").pack()
        self.voice_entry = tk.Entry(self.root)
        self.voice_entry.insert(0, "en")
        self.voice_entry.pack()

        self.speed = self.add_slider("Speed (80–450)", 80, 450, 300)
        self.pitch = self.add_slider("Pitch (0–99)", 0, 99, 50)
        self.amplitude = self.add_slider("Amplitude (0–200)", 0, 200, 100)
        self.gap = self.add_slider("Gap (0–100)", 0, 100, 10)

        tk.Button(self.root, text="Speak Clipboard", command=self.safe(app.speak_clipboard)).pack(pady=10)
        tk.Button(self.root, text="Stop", command=self.safe(app.stop)).pack()
        tk.Button(self.root, text="Pause", command=self.safe(app.pause)).pack()
        tk.Button(self.root, text="Resume", command=self.safe(app.resume)).pack()

        self.label = tk.Label(self.root, text="Status: idle", bg="white")
        self.label.pack(pady=20)

    def add_slider(self, label, min_, max_, default):
        tk.Label(self.root, text=label).pack()
        scale = tk.Scale(self.root, from_=min_, to=max_, orient="horizontal")
        scale.set(default)
        scale.pack()
        return scale

    def get_settings(self):
        return {
            "voice": self.voice_entry.get(),
            "speed": self.speed.get(),
            "pitch": self.pitch.get(),
            "amplitude": self.amplitude.get(),
            "gap": self.gap.get()
        }

    def safe(self, coro_func):
        def wrapper():
            settings = self.get_settings()
            self.app.update_settings(settings)
            asyncio.run_coroutine_threadsafe(coro_func(), self.app.loop)
        return wrapper

    def set_status(self, text):
        self.label.config(text=f"Status: {text}")

    def run(self):
        self.root.mainloop()
