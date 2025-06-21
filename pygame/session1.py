import pygame
pygame.init()

WIDTH  = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
pygame.mixer.music.load("./assets/sounds/jungle.wav")
pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1)

# my_font = pygame.font.Font("./assets/fonts/joystix monospace.otf", 23)
# welcome_text = my_font.render("welcome", True, (255, 0,0))
FPS = 60
clock = pygame.time.Clock()
square = pygame.Rect(100, 100, 50, 50)
go_down, go_up, go_left, go_right = (False, False, False, False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and square.top > 0:
        square.y -= 10
    if keys[pygame.K_DOWN] and square.bottom < HEIGHT:
        square.y += 10
    if keys[pygame.K_LEFT]:
        square.x -= 10
    if keys[pygame.K_RIGHT]:
        square.x += 10
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), square)
    pygame.display.update()
    clock.tick(FPS)