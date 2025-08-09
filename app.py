import pvporcupine
from dotenv import load_dotenv
from os import getenv

load_dotenv()
PORCUPINE_ACCESS_KEY = getenv("PORCUPINE_ACCESS_KEY")

def main():
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_ACCESS_KEY,
        keyword_paths=["./models/Sunshine_en_windows_v3_0_0.ppn"]
    )