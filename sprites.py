#####################################################
##                   sprites.py                    ##
##                   Ocean Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 3.8.2 32-bit              ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame as pg
import time, random
from os import path
from settings import *
from tilemap import *
vec = pg.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - (sprite.hit_rect.width / 2) # dividing by 2 because we are using the center
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + (sprite.hit_rect.width / 2) # dividing by 2 because we are using the center
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - (sprite.hit_rect.height / 2) # dividing by 2 because we are using the center
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + (sprite.hit_rect.height / 2) # dividing by 2 because we are using the center
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


def drawCharacterNextImage(sprite, images, anim_speed):
    """ Cycle through the images for this sprite
    """
    sprite.count += 1
    if sprite.currentImage >= len(images) - 1: # index needs to be 0 to 9, not 1 to 10
        sprite.currentImage = 0
    sprite.image = images[sprite.currentImage].convert_alpha()
    if sprite.count > anim_speed:
        sprite.currentImage += 1
        sprite.count = 0


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.currentImage = 0
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
        self.count = 0 # used to animate the sprite at a slower speed than the game speed

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
            drawCharacterNextImage(self, PLAYER_IMAGES, PLAYER_ANIMATION_SPEED)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
            drawCharacterNextImage(self, PLAYER_IMAGES, PLAYER_ANIMATION_SPEED)
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot) # move in the direction we have rotated to
            drawCharacterNextImage(self, PLAYER_IMAGES, PLAYER_ANIMATION_SPEED)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 4, 0).rotate(-self.rot) # move in the opposite direction we have rotated to
            drawCharacterNextImage(self, PLAYER_IMAGES, PLAYER_ANIMATION_SPEED)

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360 # rotates the player rect
        self.game.player_img = PLAYER_IMAGES[self.currentImage].convert_alpha()
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect() # to center around the new rect
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x # using center because it's the center of the player we want to track
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y # using center because it's the center of the player we want to track
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

class Turtle(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.turtles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.currentImage = 0
        self.image = game.turtle_img
        self.rect = self.image.get_rect()
        self.hit_rect = TURTLE_HIT_RECT.copy() # copy is required because you'll likely have multiple turples, so you need to use copies instead
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0 # facing right when it spawns
        self.rot_speed = TURTLE_ROT_SPEED
        self.count = 0 # used to animate the sprite at a slower speed than the game speed

    def update(self):
        self.rot = (self.pos - self.game.player.pos).angle_to(vec(1,0))
        #self.rot = ((self.rot + self.rot_speed * self.game.dt) + random.uniform(-1, 1)) % 360 # rotates the player rect # + random.uniform(-1, 1) # 
        self.image = pg.transform.rotate(self.game.turtle_img, self.rot)
        self.rect = self.image.get_rect() # to center around the new rect
        self.rect.center = self.pos
        self.acc = vec(TURTLE_SPEED, 0).rotate(-self.rot)
        self.acc += self.vel * -1 # add some friction, to slow down the speed
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        drawCharacterNextImage(self, TURTLE_IMAGES, TURTLE_ANIMATION_SPEED)

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE