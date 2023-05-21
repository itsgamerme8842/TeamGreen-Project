def Jump_and_Gravity():
    scene.camera_follow_sprite(mySprite)
    mySprite.ay = 200
    if controller.A.is_pressed():
        if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
            mySprite.vy = -100
def Turn_Right_Char():
    global Location, Location_y, mySprite, LR
    if LR == 1:
        Location = mySprite.x
        Location_y = mySprite.y
        sprites.destroy(mySprite)
        mySprite = sprites.create(assets.image("""
            myImage0
        """), SpriteKind.player)
        mySprite.set_position(Location, Location_y)
        mySprite.set_stay_in_screen(True)
        controller.move_sprite(mySprite, 100, 0)
        LR = 0

def on_left_pressed():
    Turn_Left_Char()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    Turn_Right_Char()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_menu_pressed():
    global MENU
    MENU = 1
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

MENU = 0
mySprite: Sprite = None
LR = 0
Location = 0
Location_y = 0
def Turn_Left_Char(menuvar: any = None):
    global Location, Location_y, mySprite, LR
    if LR == 0:
        Location = mySprite.x
        Location_y = mySprite.y
        sprites.destroy(mySprite)
        mySprite = sprites.create(assets.image("""
            myImage
        """), SpriteKind.player)
        mySprite.set_position(Location, Location_y)
        controller.move_sprite(mySprite, 100, 0)
        mySprite.set_stay_in_screen(True)
        LR = 1
MENU = 0
mySprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
scene.set_background_color(9)
tiles.set_current_tilemap(tilemap("""
    level
"""))
LR = 1

def on_forever():
    Jump_and_Gravity()
forever(on_forever)
