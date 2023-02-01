import pygame

pygame.init()

window = pygame.display.set_mode((1280, 720))
window_title = pygame.display.set_caption('Futebol Caraio')

field = pygame.image.load('/home/phllp/dev/bootcamp_python/modulo_04/game_dev/assets/field.jpg')
window.blit(field, (0,0))

player_one = pygame.image.load('/home/phllp/dev/bootcamp_python/modulo_04/game_dev/assets/player01nobg.png')
player_one_y = 310
player_one_moveup = False
player_one_movedown = False

player_two = pygame.image.load('/home/phllp/dev/bootcamp_python/modulo_04/game_dev/assets/player01nobg.png')
player_two_y = 310

ball = pygame.image.load('/home/phllp/dev/bootcamp_python/modulo_04/game_dev/assets/ball.png')
ball_x = 617
ball_y = 337
ball_dir = -3
ball_dir_y = 1

def move_player():
  global player_one_y

  if player_one_moveup:
    player_one_y -= 5
  else: 
    player_one_y += 0
    
  if player_one_movedown:
    player_one_y += 5
  else: 
    player_one_y += 0
    
  if player_one_y <= 0:
    player_one_y = 0
  elif player_one_y >= 520: 
    player_one_y = 520

def move_player_two():
  global player_two_y
  player_two_y = ball_y

ball_x = 600
ball_y = 310

def move_ball():
  global ball_x
  global ball_y
  global ball_dir
  global ball_dir_y

  ball_x += ball_dir
  ball_y += ball_dir_y

  if ball_x < 120:
    if player_one_y < ball_y + 23:
      if player_one_y + 146 > ball_y:
        ball_dir *= -1
  
  if ball_x > 1100:
    if player_two_y < ball_y + 23:
      if player_two_y + 146 > ball_y:
        ball_dir *= -1

  if ball_y > 685:
    ball_dir_y *= -1
  elif ball_y <= 0:
    ball_dir_y *= -1
  

def drawn():
  window.blit(field, (0,0))
  window.blit(player_one, (70, player_one_y))
  window.blit(player_two, (1050,player_two_y))
  window.blit(ball, (ball_x, ball_y))


loop = True

while loop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      loop = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        player_one_moveup = True
      if event.key == pygame.K_s:
        player_one_movedown = True
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_w:
        player_one_moveup = False
      if event.key == pygame.K_s:
        player_one_movedown = False
  if Event.get==keydown:
    print('nois')
  move_ball()
  move_player()
  move_player_two()
  drawn()
  pygame.display.update()