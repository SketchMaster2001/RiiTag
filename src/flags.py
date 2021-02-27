from main import app, db
from PIL import Image
from models import UserData


background = Image.open("assets/temp/bck.png")
flag = Image.open("assets/flags/ca.png")

flag = flag.convert('RGBA')

background.paste(flag, (12, 10), flag)

background.save('assets/temp/flag.png')





