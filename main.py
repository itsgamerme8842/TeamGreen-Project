@namespace
class StatusBarKind:
    O2 = StatusBarKind.create()

def on_b_pressed():
    statusbar.value += 15
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def Jump_and_Gravity():
    scene.camera_follow_sprite(mySprite)
    mySprite.ay = 200
    if controller.A.is_pressed():
        if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
            mySprite.vy = -100
            statusbar.value += -3
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
        statusbar.attach_to_sprite(mySprite)
        LR = 0

def on_left_pressed():
    Turn_left_Char()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def Spawn_c02():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)

def on_right_pressed():
    Turn_Right_Char()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_menu_pressed():
    global MENU
    MENU = 1
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def Turn_left_Char():
    global Location, Location_y, mySprite, LR
    if LR == 0:
        Location = mySprite.x
        Location_y = mySprite.y
        sprites.destroy(mySprite)
        mySprite = sprites.create(assets.image("""
            myImage
        """), SpriteKind.player)
        mySprite.set_position(Location, Location_y)
        mySprite.set_stay_in_screen(True)
        controller.move_sprite(mySprite, 100, 0)
        statusbar.attach_to_sprite(mySprite)
        LR = 1
mySprite2: Sprite = None
Location_y = 0
Location = 0
statusbar: StatusBarSprite = None
LR = 0
mySprite: Sprite = None
MENU = 0
MENU = 0
mySprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
scene.set_background_color(9)
tiles.set_current_tilemap(tilemap("""
    level
"""))
LR = 1
statusbar = statusbars.create(20, 4, StatusBarKind.O2)
statusbar.attach_to_sprite(mySprite)
statusbar.set_label("O2")
statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)

def on_forever():
    Jump_and_Gravity()
forever(on_forever)

def on_forever2():
    statusbar.value += -1
    pause(100)
    if statusbar.value <= 0:
        sprites.destroy(mySprite)
forever(on_forever2)
