#####################################################
##                   sprites.py                    ##
##                   Ocean Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 3.8.2 32-bit              ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame as pg
from os import path
from settings import *
from tilemap import *
vec = pg.math.Vector2

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

    #def drawCharacterNextImage(self):
     #   """ Cycle through the images for this sprite
     #   """
     #   pass
        #self.currentImage += 1
        #if self.currentImage >= len(PLAYER_IMAGES):
        #    self.currentImage = 0
        #self.image = pg.image.load(path.join(PLAYER_IMG_FOLDER, PLAYER_IMAGES[self.currentImage])).convert_alpha()

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
            #self.drawCharacterNextImage()
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
            #self.drawCharacterNextImage()
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot) # move in the direction we have rotated to
            #self.drawCharacterNextImage()
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 4, 0).rotate(-self.rot) # move in the opposite direction we have rotated to
            #self.drawCharacterNextImage()

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - (self.hit_rect.width / 2) # dividing by 2 because we are using the center
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + (self.hit_rect.width / 2) # dividing by 2 because we are using the center
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - (self.hit_rect.height / 2) # dividing by 2 because we are using the center
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + (self.hit_rect.height / 2) # dividing by 2 because we are using the center
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360 # rotates the player rect
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect() # to center around the new rect
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x # using center because it's the center of the player we want to track
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y # using center because it's the center of the player we want to track
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE