import asyncio
import subprocess

class SpeechManager:
    def __init__(self):
        self.proc = None
        self.paused = False
        self.settings = {
            "voice": "en",
            "speed": 300,
            "pitch": 50,
            "amplitude": 100,
            "gap": 10
        }

    def set_settings(self, new_settings):
        self.settings.update(new_settings)

    async def speak(self, text):
        await self.stop()
        if not text:
            text = "Clipboard is empty"

        args = [
            "espeak",
            f"-v{self.settings['voice']}",
            f"-s{self.settings['speed']}",
            f"-p{self.settings['pitch']}",
            f"-a{self.settings['amplitude']}",
            f"-g{self.settings['gap']}",
            text
        ]

        self.proc = await asyncio.create_subprocess_exec(
            *args,
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
        if self.proc and self.proc.returncode is None:
            await self.stop()
            self.paused = True

    async def resume(self, text):
        if self.paused:
            await self.speak(text)
