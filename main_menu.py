import pygame
import sys
from button import Button

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('Menu Test Resizable')

# BACKGROUND = pygame.image.load('sunset_test.jpg')
# screen_size = screen.get_size()
# BACKGROUND_SCALED = pygame.transform.scale(BACKGROUND, screen_size)

# sprite_sheet = pygame.image.load('assets/11.png').convert_alpha()
# sprite_rect = pygame.Rect(79, 143, 81, 32)

# sprite_image = pygame.Surface((81, 32), pygame.SRCALPHA)

# sprite_image.blit(sprite_sheet, (0, 0), sprite_rect)

# scale_factor = 4
# scaled_image = pygame.transform.scale(sprite_image, (81 * scale_factor, 32 * scale_factor))


def get_font(size):
    return pygame.font.Font("fonts/Grand9K Pixel.ttf", size)
    # font_name: Grand9k Pixel/grand9k_pixel

def play():
    screen.fill('white')
    PLAYER_MOUSE_POS = pygame.mouse.get_pos()

    PLAYER_SCREEN_TEXT = get_font(35).render('''Welcome to PYSEAS! 
            A great adventure lies ahead!''', True, 'black')
    PS_RECT = PLAYER_SCREEN_TEXT.get_rect(center=(420, 300))

    back_button_surface = pygame.Surface((100, 100))
    back_button_surface.fill('white')

    BACK_BUTTON = Button(image=back_button_surface, pos=(100, 550), text_input="< Back", 
                            font=get_font(40), base_color='grey', hovering_color='black')
    
    for button in [BACK_BUTTON]:
        button.changeColor(PLAYER_MOUSE_POS)
        button.update(screen)

    screen.blit(PLAYER_SCREEN_TEXT, PS_RECT)

    return BACK_BUTTON

def options():
    screen.fill('white')
    OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

    OPT_SCREEN_TXT = get_font(35).render('''Here you can find OPTIONS''', True, 'black')
    OPT_RECT = OPT_SCREEN_TXT.get_rect(center=(520, 550))

    # TO DO: Adjust the button surface so it doesnt overlap with the other surfaces (DONE)

    back_button_surface = pygame.Surface((100, 100))
    back_button_surface.fill('white')

    res_button_surface = pygame.Surface((150, 100))
    res_button_surface.fill('white')

    sfx_button_surface = pygame.Surface((150, 100))
    sfx_button_surface.fill('white')

    diff_button_surface = pygame.Surface((150, 100))
    diff_button_surface.fill('white')

    BACK_BUTTON = Button(image=back_button_surface, pos=(100, 550), text_input="< Back", 
                            font=get_font(40), base_color='grey', hovering_color='black')
    
    RES_BUTTON = Button(image=res_button_surface, pos=(150, 50), text_input='Resolution',
                        font=get_font(40), base_color='grey', hovering_color='black')
    
    SFX_BUTTON = Button(image=res_button_surface, pos=(100, 200), text_input='Sound',
                        font=get_font(40), base_color='grey', hovering_color='black')
    
    DIFF_BUTTON = Button(image=res_button_surface, pos=(135, 350), text_input='Difficulty',
                        font=get_font(40), base_color='grey', hovering_color='black')
    
    for button in [BACK_BUTTON, RES_BUTTON, SFX_BUTTON, DIFF_BUTTON]:
        button.changeColor(OPTIONS_MOUSE_POS)
        button.update(screen)

    screen.blit(OPT_SCREEN_TXT, OPT_RECT)

    return BACK_BUTTON, RES_BUTTON, SFX_BUTTON, DIFF_BUTTON

def res():
    screen.fill('white')

    RES_MOUSE_POS = pygame.mouse.get_pos()

    RES_TEXT = get_font(50).render('RESOLUTION', True, 'black')
    RES_RECT = RES_TEXT.get_rect(center=(420, 100))

    fhd_button_surface = pygame.Surface((200, 100))
    fhd_button_surface.fill('white')
    hd_button_surface = pygame.Surface((200, 100))
    hd_button_surface.fill('white')
    third_button_surface = pygame.Surface((200, 100))
    third_button_surface.fill('white')
    back_button_surface = pygame.Surface((100, 100))
    back_button_surface.fill('white')

    FHD_BUTTON = Button(image=fhd_button_surface, pos=(200, 200), text_input="1920x1080", font=get_font(35), base_color='grey', hovering_color='black')
    HD_BUTTON = Button(image=hd_button_surface, pos=(200, 300), text_input="1280x720", font=get_font(35), base_color='grey', hovering_color='black')
    THIRD_BUTTON = Button(image=third_button_surface, pos=(200, 400), text_input="800x600", font=get_font(35), base_color='grey', hovering_color='black')
    BACK_BUTTON = Button(image=back_button_surface, pos=(100, 550), text_input="< Back", 
                            font=get_font(40), base_color='grey', hovering_color='black')

    for button in [FHD_BUTTON, HD_BUTTON, THIRD_BUTTON, BACK_BUTTON]:
        button.changeColor(RES_MOUSE_POS)
        button.update(screen)

    screen.blit(RES_TEXT, RES_RECT)

    return BACK_BUTTON

def diff():
    screen.fill('white')

    DIFF_MOUSE_POS = pygame.mouse.get_pos()

    DIFF_TEXT = get_font(50).render('DIFFICULTY', True, 'black')
    DIFF_RECT = DIFF_TEXT.get_rect(center=(380, 100))

    easy_button_surface = pygame.Surface((200, 100))
    easy_button_surface.fill('white')
    medium_button_surface = pygame.Surface((200, 100))
    medium_button_surface.fill('white')
    hard_button_surface = pygame.Surface((200, 100))
    hard_button_surface.fill('white')
    back_button_surface = pygame.Surface((100, 100))
    back_button_surface.fill('white')

    EASY_BUTTON = Button(image=easy_button_surface, pos=(380, 200), text_input="Easy", font=get_font(35), base_color='grey', hovering_color='black')
    MEDIUM_BUTTON = Button(image=medium_button_surface, pos=(380, 300), text_input="Medium", font=get_font(35), base_color='grey', hovering_color='black')
    HARD_BUTTON = Button(image=hard_button_surface, pos=(380, 400), text_input="Hard", font=get_font(35), base_color='grey', hovering_color='black')
    BACK_BUTTON = Button(image=back_button_surface, pos=(100, 550), text_input="< Back", font=get_font(40), base_color='grey', hovering_color='black')

    for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
        button.changeColor(DIFF_MOUSE_POS)
        button.update(screen)

    screen.blit(DIFF_TEXT, DIFF_RECT)

    return BACK_BUTTON


def main_menu():
    screen.fill('black')

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render('MAIN MENU', True, 'white')
    MENU_RECT = MENU_TEXT.get_rect(center=(420, 100))

    # play_button_surface = pygame.Surface((300, 100))
    # play_button_surface.fill("brown")

    play_button_surface = pygame.Surface((370, 100))
    # play_button_surface.fill("brown")
    opt_button_surface = pygame.Surface((370, 100))
    # opt_button_surface.fill("brown")
    quit_button_surface = pygame.Surface((220, 100))
    # quit_button_surface.fill("brown")

    PLAY_BUTTON = Button(image=play_button_surface, 
                            pos=(200, 250), text_input='PLAY', font=get_font(45), base_color='white', hovering_color='grey')
    
    OPT_BUTTON = Button(image=opt_button_surface, 
                        pos=(240, 360), text_input='OPTIONS', font=get_font(45), base_color='white', hovering_color='grey')
    
    QUIT_BUTTON = Button(image=quit_button_surface, 
                        pos=(190, 470), text_input='QUIT', font=get_font(45), base_color='white', hovering_color='grey')
    
    screen.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, OPT_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)

    return PLAY_BUTTON, OPT_BUTTON, QUIT_BUTTON


run = True
state = 'main_menu'
while run:

    # pygame.draw.rect(screen, 'blue', (200, 200, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == 'main_menu':
                PLAY_BUTTON, OPT_BUTTON, QUIT_BUTTON = main_menu()
                if PLAY_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'play'
                elif OPT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'options'
                elif QUIT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

            elif state == 'play':
                BACK_BUTTON = play()
                if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'main_menu'

            elif state == 'options':
                BACK_BUTTON, RES_BUTTON, SFX_BUTTON, DIFF_BUTTON = options()
                if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'main_menu'
                elif RES_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'res'
                elif DIFF_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'diff'

            elif state == 'diff':
                BACK_BUTTON = diff()
                if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'options'

            elif state == 'res':
                BACK_BUTTON = res()
                if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    state = 'options'

    if state == 'main_menu':
        main_menu()
    elif state == 'play':
        play()
    elif state == 'options':
        options()
    elif state == 'res':
        res()
    elif state == 'diff':
        diff()

    # pygame.display.update()

    pygame.display.flip()
pygame.quit()
