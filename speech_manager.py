import asyncio
from events import Event

class SpeechManager:
    def __init__(self):
        self.proc = None

    async def handle_event(self, event, event_queue):
        if event is Event.CTRL_C_PRESSED:
            print("Ctrl+C event received in SpeechManager")
            await self.toggle_speech(event_queue)

    async def toggle_speech(self, event_queue):
        # If speaking, stop. Else, start.
        if self.proc and self.proc.returncode is None:
            self.proc.terminate()
            await self.proc.wait()
        else:
            # enqueue an event to show overlay
            event_queue.put_nowait(Event.SHOW_OVERLAY)
            self.proc = await asyncio.create_subprocess_exec(
                'espeak', 'Hello there',
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL
            )
