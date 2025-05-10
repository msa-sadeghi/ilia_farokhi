import pygame
pygame.init()

WIDTH  = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
pygame.mixer.music.load("./assets/sounds/jungle.wav")
pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1)

my_font = pygame.font.Font("./assets/fonts/joystix monospace.otf", 23)
welcome_text = my_font.render("welcome", True, (255, 0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(welcome_text,  (100, 300))
    pygame.draw.rect(screen, "green", (200, 200, 100, 300), 5, 100)
    pygame.draw.rect(screen, "green", (400, 200, 100, 300))
    pygame.draw.line(screen, "purple", (300, 300), (600, 600), 10)
    pygame.draw.ellipse(screen, "yellow", (150, 400, 100, 100))
    pygame.display.update()