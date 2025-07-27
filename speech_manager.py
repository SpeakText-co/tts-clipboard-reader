import asyncio
import subprocess

class SpeechManager:
    def __init__(self):
        self.proc = None
        self.paused = False

    async def speak(self, text):
        await self.stop()
        if not text:
            text = "Clipboard is empty"
        self.proc = await asyncio.create_subprocess_exec(
            'espeak', text,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    async def stop(self):
        if self.proc and self.proc.returncode is None:
            self.proc.terminate()
            await self.proc.wait()
        self.proc = None
        self.paused = False

    async def pause(self):
        # Can't pause espeak natively, but you can fake it by stopping
        if self.proc and self.proc.returncode is None:
            await self.stop()
            self.paused = True

    async def resume(self, text):
        if self.paused:
            await self.speak(text)
