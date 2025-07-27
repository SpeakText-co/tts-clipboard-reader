import asyncio
import threading
import tkinter as tk

from input_listener import start_listener
from speech_manager import SpeechManager
from clipboard_reader import get_clipboard_text
from gui import ControlUI
from events import Event

class App:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.speech = SpeechManager()
        self.last_clipboard = ""
        self.ui = ControlUI(self)

    def update_settings(self, settings):
        self.speech.set_settings(settings)

    def start(self):
        # Start asyncio + input listener in background thread
        threading.Thread(target=self._start_async_parts, daemon=True).start()

        # Start GUI in the main thread
        self.ui.run()

    def _start_async_parts(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.loop = loop

        # Start pynput key listener
        start_listener(self.queue, loop)

        loop.run_until_complete(self.event_loop())

    async def event_loop(self):
        while True:
            event = await self.queue.get()
            if event == Event.CLIPBOARD_TRIGGER:
                await self.speak_clipboard()
            elif event == Event.STOP:
                await self.stop()
            elif event == Event.TOGGLE_PAUSE:
                if self.speech.paused:
                    await self.resume()
                else:
                    await self.pause()

    async def speak_clipboard(self):
        self.last_clipboard = get_clipboard_text()
        self.ui.set_status("Speaking")
        await self.speech.speak(self.last_clipboard)

    async def stop(self):
        await self.speech.stop()
        self.ui.set_status("Stopped")

    async def pause(self):
        await self.speech.pause()
        self.ui.set_status("Paused")

    async def resume(self):
        await self.speech.resume(self.last_clipboard)
        self.ui.set_status("Speaking")

if __name__ == "__main__":
    App().start()
