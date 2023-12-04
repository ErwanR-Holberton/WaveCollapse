import pygame
class Button:

    number_of_buttons = 0
    size = 12
    color = (255, 255, 255)
    state = 1
    font = pygame.font.Font(None, 18)

    def __init__(self, name):
        self.x = 16 * 20 + 10
        self.y = 10 + 20 * self.__class__.number_of_buttons
        self.rectvalue = (self.x, self.y, self.size, self.size)
        self.text_pos = (self.x + self.size + 5, self.y)
        self.name = name
        self.text = self.font.render(name, True, (150, 150, 150))
        self.__class__.number_of_buttons += 1
        pass

    def is_in(self, mouse_x, mouse_y):
        if mouse_x < self.x or mouse_x > self.x + self.size:
            return 0
        if mouse_y < self.y or mouse_y > self.y + self.size:
            return 0
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1
        return 1
