import pvporcupine
from pvrecorder import PvRecorder
from dotenv import load_dotenv
from os import getenv

load_dotenv()
PORCUPINE_ACCESS_KEY = getenv("PORCUPINE_ACCESS_KEY")

def main():

    try:
        porcupine = pvporcupine.create(
            access_key=PORCUPINE_ACCESS_KEY,
            keyword_paths=["./models/Sunshine_en_windows_v3_0_0.ppn"]
        )

    except pvporcupine.PorcupineError as err:
        print(f"ERROR: {err.message}")

    recorder = PvRecorder(porcupine.frame_length)
    recorder.start()


    try:
        while True:
            pcm = recorder.read()
            res = porcupine.process(pcm)

            if res >= 0:
                print("Detected keyword")
                
                response = listenForStatement()

    except KeyboardInterrupt:
        print("Halting Program...")

    finally:
        recorder.delete()
        porcupine.delete()

if __name__ == "__main__":
    main()