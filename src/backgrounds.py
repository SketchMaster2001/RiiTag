from main import app, db 
from PIL import Image
from models import UserData


def serve_background(discord_id):
    retrieved_data = (          
        db.session.query(UserData)
        .filter(UserData.discord_id == discord_id)
        .all
    )
    for user_data in enumerate(retrieved_data):
        bg = user_data.background
        overly = user_data.overlay
    
    
    background = Image.open(f"assets/backgrounds/{bg}.jpg").format(bg)
    overlay = Image.open(f"assets/overlays/{overly}.png").format(overly) 
    
    background.paste(overlay, (0, 0), overlay)
    background.save('assets/temp/bck.png').format(discord_id)



