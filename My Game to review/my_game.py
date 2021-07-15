# Importing the pygame modules and random module
import pygame 
import random

# Initialize the pygame modules
pygame.init() 

# The game windiow
# To get the game window we give it a height and width in the variables "screen_width" and "screen_height"
# Call on the display module in pygames to make the screen and give it the variables "screen_width" and "screen_height"
screen_width = 1100
screen_height = 840
screen = pygame.display.set_mode((screen_width, screen_height))

# Creating the player
# Load the image you want the "player" to be
# Then get the height and width of the image using the ".get_height" and ".get_width" method
# Give the "playe"r a posistion on the game window using the Y axis and X axis of the game window
player = pygame.image.load("player.png")    # Reference at recourses
player_height = player.get_height()
player_width = player.get_width()
player_x_Position = 10
player_y_Position = 400

# Creating enemy 1
# Load the image you want the "enemy" to be
# Then get the height and width of the image using the ".get_height" and ".get_width" method
# Give the "enemy" a posistion on the game window using the Y axis and X axis of the game window
# Use the random function to generate random numbers between the 2 given numbers "(0, 152)"
# Give the numbers so that the enemies will not overlap eachother
enemy = pygame.image.load("enemy.png")  # Reference at recourses
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy_x_Position =  screen_width - enemy_width
enemy_y_Position =  random.randint(0, 152)

# Creating enemy 2
# Load the image you want the "enemy2" to be
# Then get the height and width of the image using the ".get_height" and ".get_width" method
# Give the "enemy2" a posistion on the game window using the Y axis and X axis of the game window
# Use the random function to generate random numbers between the 2 given numbers "(280, 408)"
# Give the numbers so that the enemies will not overlap eachother
enemy2 = pygame.image.load("enemy.png")     # Reference at recourses
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy2_x_Position =  screen_width - enemy2_width
enemy2_y_Position =  random.randint(280, 408)

# Creating enemy 3
# Load the image you want the "enemy3" to be
# Then get the height and width of the image using the ".get_height" and ".get_width" method
# Give the "enemy3" a posistion on the game window using the Y axis and X axis of the game window
# Use the random function to generate random numbers between the 2 given numbers "(563, 644)"
# Give the numbers so that the enemies will not overlap eachother
enemy3 = pygame.image.load("enemy.png")     # Reference at recourses
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
enemy3_x_Position =  screen_width - enemy3_width
enemy3_y_Position =  random.randint(563,  644)

# Creating the prize
# Load the image you want the "prize" to be
# Then get the height and width of the image using the ".get_height" and ".get_width" method
# Give the "priz"e a posistion on the game window using the Y axis and X axis of the game window
# The "prizeXPosition" will appear against the right side of the game window
# Int the prizeYPosition a random number is generated so that the prize will appear randomly on the Y axis
prize = pygame.image.load("prize.png")  # Reference at recourses
prize_height = prize.get_height()
prize_width = prize.get_width()
prize_x_Position = screen_width - prize_width
prize_y_Position = random.randint(0, screen_height - prize_height)

# This checks if the up, down, left or right key is pressed.
# Give them the bolean value of "False" to start with, because they are not pressed 
key_up= False
key_down = False
key_left = False
key_right = False

# The game loop
# This will be an infinited loop, everything in this whlie loop will run over and over again untill the condition of "exit" is given or met
while 1:
    # The game window is made white to see the images better
    # Used the RGB for white to make the game window white
    screen.fill((255, 255, 255))
    # The "player", "enemy", "enemy2", "enemy3" and "prize" is drawn on to the game window
    # Everything is given there Y axis and X axis variables to show where they need to print on the game window
    screen.blit(player, (player_x_Position, player_y_Position))
    screen.blit(enemy, (enemy_x_Position, enemy_y_Position))
    screen.blit(enemy2, (enemy2_x_Position, enemy2_y_Position))
    screen.blit(enemy3, (enemy3_x_Position, enemy3_y_Position))
    screen.blit(prize, (prize_x_Position, prize_y_Position))
    # This updates the screen
    pygame.display.flip() 
    
    # This loops through events in the game    
    for event in pygame.event.get():    
        # This event checks if the user quits the program, then if so it exits the program.        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press any key on the keyboard        
        if event.type == pygame.KEYDOWN:        
            # Test if the key pressed is the one we want
            # If the key is pressed that we want, the variables are given the value of "True"
            if event.key == pygame.K_UP:  
                key_up = True
            elif event.key == pygame.K_DOWN:
                key_down = True
            elif event.key == pygame.K_LEFT:
                key_left = True
            elif event.key == pygame.K_RIGHT:
                key_right = True                
        # This event checks if the key is not pressed or released by the user        
        if event.type == pygame.KEYUP:        
            # Test if the key released is the one we want
            # If the pressed key is released, the variables below are given the value of "False"
            if event.key == pygame.K_UP: 
                key_up = False
            elif event.key == pygame.K_DOWN:
                key_down = False
            elif event.key == pygame.K_LEFT:
                key_left = False
            elif event.key == pygame.K_RIGHT:
                key_right = False
                
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # If you want to move down you have to increase the Y axis value and up is decreasing the Y axis value
    # If you want to move right you have to increase the X axis value and left is decreasing the X axis value
    # If the key variables values are "True" they will move according to the direction of the key
    # In all the nested if statements we just make sure that the "player" can not leave the screen, and just stops at the border of the game window    
    if key_up == True:
        if player_y_Position > 0 :        
            player_y_Position += -1
    if key_down == True:
        if player_y_Position < screen_height - player_height:         
            player_y_Position += 1
    if key_left == True:
        if player_x_Position > 0:
            player_x_Position += -1
    if key_right == True:
        if player_x_Position < screen_width - player_width:
            player_x_Position += 1
    
    
    # Bounding box for the player:
    # Create a rectangle around the "player"
    # Give the rectangle the coordinates of the "player" so that it can follow its movement
    player_Box = pygame.Rect(player.get_rect())
    player_Box.top = player_y_Position
    player_Box.left = player_x_Position

    
    
    # Bounding box for the enemy:
    # Create a rectangle around the "enemy"
    # Give the rectangle the coordinates of the "enemy" so that it can follow its movement
    # Then we decrease the X axis value so that the "enemy" moves towards the left of the game window
    enemy_Box = pygame.Rect(enemy.get_rect())
    enemy_Box.top = enemy_y_Position
    enemy_Box.left = enemy_x_Position
    enemy_x_Position += -0.40


    # Bounding box for the enemy 2:
    # Create a rectangle around the "enemy2"
    # Give the rectangle the coordinates of the "enemy2" so that it can follow its movement
    # Then we decrease the X axis value so that the "enemy2" moves towards the left of the game window    
    enemy2_Box = pygame.Rect(enemy2.get_rect())
    enemy2_Box.top = enemy2_y_Position
    enemy2_Box.left = enemy2_x_Position
    enemy2_x_Position += -0.40

    
    # Bounding box for the enemy 3:
    # Create a rectangle around the "enemy3"
    # Give the rectangle the coordinates of the "enemy3" so that it can follow its movement
    # Then we decrease the X axis value so that the "enemy3" moves towards the left of the game window    
    enemy3_Box = pygame.Rect(enemy3.get_rect())
    enemy3_Box.top = enemy3_y_Position
    enemy3_Box.left = enemy3_x_Position
    enemy3_x_Position += -0.40




    # Bounding box for prize:
    # Create a rectangle around the "prize"
    # Give the rectangle the coordinates of the "prize" so that it can follow its movement
    # The prize has no movement in the game, and is only placedd on a random spot on the Y axis every iteration of the game
    prize_Box = pygame.Rect(prize.get_rect())
    prize_Box.top = prize_y_Position
    prize_Box.left = prize_x_Position


        
    
    # Test collision of the boxes:
    # If the "player" rectangle collides with any of the enemies rectangles, the game wil print "You lose!" and exit the program
    if player_Box.colliderect(enemy_Box) or player_Box.colliderect(enemy2_Box) or player_Box.colliderect(enemy3_Box):        
        print("You lose!")        
        pygame.quit()
        exit(0)
    
    # If the "player" rectangle collides with the "prize: rectangle, the game will print "You win!" and exit the program
    if player_Box.colliderect(prize_Box): 
        print("You win!")
        pygame.quit()
        exit(0)    
    # ================The game loop logic ends here. =============

# Recources:
# Prize icon
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# Enemy icon
# <div>Icons made by <a href="https://www.flaticon.com/authors/payungkead" title="Payungkead">Payungkead</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# Player icon
# <div>Icons made by <a href="https://www.flaticon.com/authors/eucalyp" title="Eucalyp">Eucalyp</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

  
