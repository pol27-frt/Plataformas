def on_overlap_tile(sprite3, location3):
    tiles.set_current_tilemap(tilemap("""
        level17
    """))
    tiles.place_on_tile(Fantasma, tiles.get_tile_location(1, 13))
scene.on_overlap_tile(SpriteKind.player, sprites.castle.rock0, on_overlap_tile)

def on_overlap_tile2(sprite32, location32):
    tiles.set_current_tilemap(tilemap("""
        level10
    """))
    tiles.place_on_tile(Fantasma, tiles.get_tile_location(0, 11))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        transparency16
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite33, location33):
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
    tiles.place_on_tile(Fantasma, tiles.get_tile_location(2, 12))
scene.on_overlap_tile(SpriteKind.player, sprites.castle.rock1, on_overlap_tile3)

def on_overlap_tile4(sprite2, location2):
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
    tiles.place_on_tile(Fantasma, tiles.get_tile_location(1, 12))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile4)

def on_overlap_tile5(sprite, location):
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile5)

def on_right_pressed():
    Fantasma.set_image(img("""
        ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                ......fbd1111111f.......
                ......fdd1111111df......
                ......fddd111111df......
                ......fdddddd111df......
                ......fdddddd111df......
                ......fbddddddd1df......
                ......ffbbddbfd1df......
                .......fcbbdcfddbf......
                .......fffbddccffff.....
                .......ffffcfbbb1bcf....
                ......ffffffffcd1b1f....
                ...ffffffffff..fdfdf....
                .....ffffff.....f.f.....
                ........................
                ........................
                ........................
                ........................
                ........................
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    Fantasma.set_image(img("""
        ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f1111111dbf......
                ......fd1111111ddf......
                ......fd111111dddf......
                ......fd111ddddddf......
                ......fd111ddddddf......
                ......fd1dddddddbf......
                ......fd1dfbddbbff......
                ......fbddfcdbbcf.......
                .....ffffccddbfff.......
                ....fcb1bbbfcffff.......
                ....f1b1dcffffffff......
                ....fdfdf..ffffffffff...
                .....f.f.....ffffff.....
                ........................
                ........................
                ........................
                ........................
                ........................
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_a_pressed():
    if Fantasma.is_hitting_tile(CollisionDirection.BOTTOM):
        Fantasma.vy = -120
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile6(sprite4, location4):
    tiles.set_current_tilemap(tilemap("""
        level0
    """))
    tiles.place_on_tile(Fantasma, tiles.get_tile_location(3, 8))
    enemigo(18, 15, 50)
    enemigo(13, 15, 50)
    enemigo(1, 15, 50)
    enemigo(4, 15, 50)
    enemigo(27, 9, 90)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile6)

def enemigo(col: number, fil: number, vel: number):
    global Enemigo
    Enemigo = sprites.create(img("""
            . . . . . b b b b b b . . . . . 
                    . . . b b 9 9 9 9 9 9 b b . . . 
                    . . b b 9 9 9 9 9 9 9 9 b b . . 
                    . b b 9 d 9 9 9 9 9 9 9 9 b b . 
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
                    . b d 5 3 3 3 3 3 3 3 d 5 b b . 
                    . . b d 5 d 3 3 3 3 5 5 b b . . 
                    . . . b b 5 5 5 5 5 5 b b . . . 
                    . . . . . b b b b b b . . . . .
        """),
        SpriteKind.enemy)
    tiles.place_on_tile(Enemigo, tiles.get_tile_location(col, fil))
    Enemigo.set_bounce_on_wall(True)
    Enemigo.set_velocity(vel, 0)

def on_overlap_tile7(sprite5, location5):
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_water,
    on_overlap_tile7)

def on_overlap_tile8(sprite6, location6):
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile8)

def on_on_overlap(sprite7, otherSprite):
    if Fantasma.x == 10:
        sprites.destroy(Fantasma, effects.disintegrate, 500)
        info.change_score_by(1)
    else:
        info.change_life_by(-1)
        scene.camera_shake(4, 500)
        pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

Enemigo: Sprite = None
Fantasma: Sprite = None
Fantasma = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
info.set_life(3)
controller.move_sprite(Fantasma, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
tiles.place_on_tile(Fantasma, tiles.get_tile_location(1, 12))
scene.camera_follow_sprite(Fantasma)
Fantasma.ay = 131