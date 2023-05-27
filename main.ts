namespace StatusBarKind {
    export const O2 = StatusBarKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    statusbar.value += 15
})
function Jump_and_Gravity () {
    scene.cameraFollowSprite(mySprite)
    mySprite.ay = 200
    if (controller.A.isPressed()) {
        if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
            mySprite.vy = -100
            statusbar.value += -3
        }
    }
}
function Turn_Right_Char () {
    if (LR == 1) {
        Location = mySprite.x
        Location_y = mySprite.y
        sprites.destroy(mySprite)
        mySprite = sprites.create(assets.image`myImage0`, SpriteKind.Player)
        mySprite.setPosition(Location, Location_y)
        mySprite.setStayInScreen(true)
        controller.moveSprite(mySprite, 100, 0)
        statusbar.attachToSprite(mySprite)
        LR = 0
    }
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    Turn_left_Char()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    Turn_Right_Char()
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    MENU = 1
})
function Turn_left_Char () {
    if (LR == 0) {
        Location = mySprite.x
        Location_y = mySprite.y
        sprites.destroy(mySprite)
        mySprite = sprites.create(assets.image`myImage`, SpriteKind.Player)
        mySprite.setPosition(Location, Location_y)
        mySprite.setStayInScreen(true)
        controller.moveSprite(mySprite, 100, 0)
        statusbar.attachToSprite(mySprite)
        LR = 1
    }
}
let Location_y = 0
let Location = 0
let statusbar: StatusBarSprite = null
let LR = 0
let mySprite: Sprite = null
let MENU = 0
MENU = 0
mySprite = sprites.create(assets.image`myImage`, SpriteKind.Player)
scene.setBackgroundColor(9)
tiles.setCurrentTilemap(tilemap`level`)
LR = 1
statusbar = statusbars.create(20, 4, StatusBarKind.O2)
statusbar.attachToSprite(mySprite)
statusbar.setLabel("O2")
statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
forever(function () {
    Jump_and_Gravity()
})
forever(function () {
    statusbar.value += -1
    pause(100)
    if (statusbar.value <= 0) {
        sprites.destroy(mySprite)
    }
})
