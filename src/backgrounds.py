from main import app, db
from PIL import Image
from models import UserData

from flask import send_from_directory

background = Image.open("assets/backgrounds/memes.jpg")
overlay = Image.open("assets/overlays/overlay1.png")

background.paste(overlay, (0, 0), overlay)

background.save('assets/temp/bruh.png')




