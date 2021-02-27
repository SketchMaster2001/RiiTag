from main import app, db
from PIL import Image, ImageFont, ImageDraw
from models import UserData

background = Image.open("assets/temp/coins.png")
title_font = ImageFont.truetype('assets/fonts/humming.ttf', 50)

title_text = "SketchMaster2001"

friend_code = "0000 0000 0000 0000"

image_editable = ImageDraw.Draw(background)

image_editable.text((95,20), title_text, (237, 230, 211), font=title_font)

image_editable.text((23,385), friend_code, (237, 230, 211), font=title_font)

background.save('assets/temp/tag.png')
