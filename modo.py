DEBUG = False

def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG
    
def get_mode():
    global DEBUG
    return DEBUG