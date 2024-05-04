import pygame
import pygame.gfxdraw

pygame.init()
buttons = pygame.sprite.Group()

class Button(pygame.sprite.Sprite):
    def __init__(self, screen, position, text, size,
                 colors="white on blue",
                 hover_colors="red on green",
                 horizon_padding=5.0,
                 style=1, borderc=(255, 255, 255),
                 command=lambda: print("No command activated for this button")):
        self.screen = screen
        self.horizon_padding = horizon_padding

        super().__init__()
        self.text = text
        self.command = command

        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        self.style = style
        self.borderc = borderc 

        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        buttons.add(self)

    def render(self):
        self.text_render = self.font.render(self.text, True, self.fg)
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        self.hover()
        self.click()

    def draw_button1(self):


        pygame.draw.line(self.screen, (150, 150, 150), (self.x, self.y), (self.x + self.w, self.y), 5)
        pygame.draw.line(self.screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)

        pygame.draw.line(self.screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w, self.y + self.h), 5)
        pygame.draw.line(self.screen, (50, 50, 50), (self.x + self.w, self.y + self.h), [self.x + self.w, self.y], 5)
 
        pygame.draw.rect(self.screen, self.bg, (self.x, self.y, self.w, self.h))
        self.screen.blit(self.image, (self.x, self.y))

    def draw_button2(self):

        pygame.draw.rect(self.screen, self.bg, (self.x, self.y, self.w, self.h))
        pygame.gfxdraw.rectangle(self.screen, (self.x, self.y, self.w, self.h), self.borderc)
        self.screen.blit(self.image, (self.x, self.y))

    def hover(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            
            self.colors = self.hover_colors
          
        else:
            self.colors = self.original_colors

        self.render()

    def click(self):
       
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.pressed = 1
