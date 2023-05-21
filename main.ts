function Jump_and_Gravity () {
    scene.cameraFollowSprite(mySprite)
    mySprite.ay = 200
    if (controller.A.isPressed()) {
        if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
            mySprite.vy = -100
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
        LR = 1
    }
}
let Location_y = 0
let Location = 0
let LR = 0
let mySprite: Sprite = null
let MENU = 0
MENU = 0
mySprite = sprites.create(assets.image`myImage`, SpriteKind.Player)
scene.setBackgroundColor(9)
tiles.setCurrentTilemap(tilemap`level`)
LR = 1
forever(function () {
    Jump_and_Gravity()
})
