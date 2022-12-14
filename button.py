import pygame.font

class Button:
    """ Class to build button for the game """

    def __init__(self,ai_game,msg):
        """ Initialize button attribute """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensio of button
        self.width = 200
        self.height = 50

        self.button_color = (0,135,0)
        self.text_color = (255,255,255)

        self.font = pygame.font.SysFont(None,48)

        # build buttons rect
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # button message
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """ Turn message into rendered image and center it """
        self.msg_img = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """ Draw button and then draw message """
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)