import logging
import time
import logging.config

# Get logging
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
from pyrogram import Client, __version__
from info import API_ID, API_HASH, BOT_TOKEN

MOD_LOAD = []
MOD_NOLOAD = []
SUDO = [617426792, 2024984460]
HELPABLE = {}

SESSION_PYRO = "BQAP-GEADARdat8jfcn2J6H0bTv4jS4dUfozDEC5u-3SFi_BfBF0kpaOJircqRgaQhIZT-lEQyhQVFaSy0jogVfokQncZ1oGBRfU9C9eM6Bhv3cdugkVkDc_yUlWL5jLA5qFCm500msA-Vv1WwzWUqB4ftRiV4q6r2KipbB3qZ4TZfDmJDJtYc0zWOu2pv73vU9xG189g7DCgCaAV6V6VdiEQsKjFGQao6VQU0nME39e31hQWU1X_DYDfqpW0g8fXFZwqrtyRrQuyFpOx9PtlmdD1N88F6gtX6elVLr5BP1rvnMmNbQLRYFu3uHyujI3eRMcr2-4x7FMGfNBMUZ_AwnITq6PewAAAAAkzS9oAA"
botStartTime = time.time()

# Pyrogram Bot Client
app = Client(
    "MissKatyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=5,
)

# Pyrogram UserBot Client
user = Client(
    "YasirUBot",
    session_string=SESSION_PYRO,
)
