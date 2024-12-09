# https://www.pygame.org/docs/tut/newbieguide.html
# https://www.youtube.com/watch?v=M_Hx0g5vFko
import pygame as pg

class SoftwareRenderer:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 1920, 1280
        self.halfWidht, self.heldHeight = self.width // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
    
    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))

    def run(self):
        while True:
            self.draw()
            #list comprehensions
            # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    app = SoftwareRenderer()
    app.run()
        
