from main import app, db
from PIL import Image
from models import UserData

background = Image.open("assets/temp/bck.png")
overlay = Image.open("assets/coins/animalcrossing.png")

background.paste(overlay, (862, 10), overlay)

background.save('assets/temp/bckflg.png')

