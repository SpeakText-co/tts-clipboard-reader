import asyncio
from asyncio import Queue
import threading

from input_listener import start_listener
from speech_manager import SpeechManager
from overlay import Overlay
from events import Event

async def main_loop():
    event_queue = Queue()
    speech_mgr = SpeechManager()
    overlay = Overlay()
    loop = asyncio.get_event_loop()

    # Start keyboard listener in background thread
    listener_thread = threading.Thread(target=start_listener, args=(event_queue,), daemon=True)
    listener_thread.start()

    print("✅ App running. Press Ctrl+C to toggle speech + overlay.")
    try:
        while True:
            print("Waiting for events...")
            
            event = await event_queue.get()
            print(f"Event received: {event}")
            # Broadcast to both managers
            await asyncio.gather(
                speech_mgr.handle_event(event, event_queue),
                overlay.handle_event(event, loop)
            )
    except asyncio.CancelledError:
        pass
    finally:
        # Clean up any running speech
        if speech_mgr.proc and speech_mgr.proc.returncode is None:
            speech_mgr.proc.terminate()
            await speech_mgr.proc.wait()

if __name__ == '__main__':
    try:
        asyncio.run(main_loop())
    except KeyboardInterrupt:
        print("👋 Exiting cleanly.")



