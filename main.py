#####################################################
##                     main.py                     ##
##                   Ocean Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 3.8.2 32-bit              ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from hud import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        self.map = Map(path.join(GAME_FOLDER, 'map2.lvl'))
        self.player_img = IMAGES_TO_LOAD['diver_male_01'].convert_alpha()
        self.wall_img   = IMAGES_TO_LOAD['rock_01'].convert_alpha()
        self.turtle_img = IMAGES_TO_LOAD['turtle_01'].convert_alpha()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.turtles = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '#':
                    Wall(self, col, row)
                if tile == 'T':
                    Turtle(self, col, row)
                if tile == '@':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # turtles hit player
        hits = pg.sprite.spritecollide(self.player, self.turtles, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= TURTLE_DAMAGE
            hit.vel = vec(0,0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos -= vec(TURTLE_KNOCKBACK, 0).rotate(-hits[0].rot)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        if SHOW_FTP:
            pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        if DRAW_GRID:
            self.draw_grid()
        for sprite in self.all_sprites:
            #if isinstance(sprite, Player):
            #    sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #pg.draw.rect(self.screen, WHITE, self.camera.apply(self.player), 2) # draws players rect used for collisions
        #pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2) # draws players hit rect used for collisions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        health_text_surf, health_text_rect = writeText('Health', WHITE, BLACK, 37, 13)
        self.screen.blit(health_text_surf, health_text_rect)
        draw_player_oxygen(self.screen, 120, 10, self.player.oxygen / PLAYER_OXYGEN)
        oxygen_text_surf, oxygen_text_rect = writeText('Oxygen', WHITE, BLACK, 147, 13)
        self.screen.blit(oxygen_text_surf, oxygen_text_rect)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()