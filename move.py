import pygame
import pyautogui

pygame.init()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Movendo o Mouse com Pygame")
clock = pygame.time.Clock()
moving_mouse = False

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Bom Trabalho!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 60)

text = font.render("Bom Trabalho, te amo!", True, WHITE)
text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
textSleep = font.render("Bom descanso!", True, WHITE)

clock = pygame.time.Clock()
heart_image = pygame.image.load('heart.jpg')

heart_width, heart_height = heart_image.get_size()

heart_x = (window_width - heart_width) // 2
heart_y = (window_height - heart_height) // 2


while True:
    if moving_mouse == False:
        window.fill(BLACK) 
        window.blit(heart_image, (heart_x, heart_y))
        window.blit(text, text_rect) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_g) or (event.key == pygame.K_a):
                window.fill(BLACK) 
                window.blit(textSleep, text_rect) 
                moving_mouse = True
            pygame.display.update()

    if moving_mouse:
        pyautogui.moveRel(17, 0, duration=0.25)  
        pyautogui.moveRel(-17, 0, duration=0.25)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_g) or (event.key == pygame.K_a):
                    moving_mouse = False

    pygame.display.update()
    clock.tick(60)  