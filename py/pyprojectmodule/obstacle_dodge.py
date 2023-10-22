import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WINDOW_WIDTH, WINDOW_HEIGHT = pygame.display.get_surface().get_size()

# Load images
background_image = pygame.image.load("C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\background.jpg")
player_image = pygame.image.load("C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\player02.png")
obstacle_image = pygame.image.load("C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\obstacle.png")
game_over_image = pygame.image.load("C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\game_over.jpg")
pygame.display.set_caption("Meteor Rush Game")

# Scale images to fit the window
player_width = 140
player_height = 140
player_image = pygame.transform.scale(player_image, (player_width, player_height))

obstacle_width = 160
obstacle_height = 130
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
game_over_image = pygame.transform.scale(game_over_image, (WINDOW_WIDTH,WINDOW_HEIGHT))

# Define player properties
player_x = WINDOW_WIDTH // 2 - player_width // 2
player_y = WINDOW_HEIGHT - player_height - 30
player_speed = 5

# Define obstacle properties
obstacle_x = random.randint(player_x-300,player_x+300)
obstacle_y = -obstacle_height
obstacle_speed = 4

# Define game properties
score = 0
level = 1
max_score = 10
max_level = 5
font = pygame.font.Font(None, 36)
font_exit=pygame.font.Font(None, 72)
clock = pygame.time.Clock()
popup_font = pygame.font.Font(None, 48)
popup_duration = 5  # in seconds
popup_timer = 0
show_popup =False
flag3=False
paused=False
end1=False

# Game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_p:  # Press 'P' key to pause the game
                paused = not paused  # Toggle pause state
            elif game_over and event.key == pygame.K_r:
                # Reset game
                game_over = False
                score = 0
                level = 1
                obstacle_speed = 4
                max_score=10
                max_level=5
                player_x = WINDOW_WIDTH // 2 - player_width // 2
                obstacle_x = random.randint(player_x-300,player_x+300)
                paused=False
                flag3=False
                show_popup=False
            elif flag3 and end1 and event.key == pygame.K_RETURN:
                # Reset game
                game_over = False
                score = 0
                level = 1
                obstacle_speed = 4
                max_score=10
                max_level=5
                player_x = WINDOW_WIDTH // 2 - player_width // 2
                obstacle_x = random.randint(player_x-300,player_x+300)
                paused=False
                flag3=False
                show_popup=False
                end1=False
  
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_ESCAPE]:
        running=False

    window.blit(background_image, (0, 0))

    if not game_over:
        if not paused:
        # Update obstacle position
            obstacle_y += obstacle_speed

        # Check collision with player
            if (
                obstacle_y + obstacle_height >= player_y
                and obstacle_x + obstacle_width >= player_x
                and obstacle_x <= player_x + player_width
            ):
                game_over = True

        # Check if obstacle passed the player
            if obstacle_y > WINDOW_HEIGHT:
                score += 1
                obstacle_x = random.randint(player_x-300,player_x+300)
                obstacle_y = -obstacle_height

                # Increase level
                if score > max_score and level < max_level:
                    level += 1
                    max_score += 10
                    obstacle_speed += 1
                    show_popup=True
                    popup_timer=pygame.time.get_ticks()
                elif level in [5,10,15] and score>50:
                    if level==5:
                        end="1 st"
                    elif level==10:
                        end='2 nd'
                    elif level==15:
                        end='3 rd'
                    
                    flag3 = True 
                    popup_timer = pygame.time.get_ticks()  # Start the popup timer


        # Draw player
        window.blit(player_image, (player_x, player_y))

        # Draw obstacle
        window.blit(obstacle_image, (obstacle_x, obstacle_y))

        # Display score and level
        score_text = font.render(f"Score: {score}", True, (255, 255,255))
        level_text = font.render(f"Level: {level}", True, (255, 255,255))
        window.blit(score_text, (10, 10))
        window.blit(level_text, (10, 50))
        
        pause_text = font.render(f"press P to pause", True, (255,0,0))
        exit_text = font.render(f"press Esc to exit", True, (255,0,0))
        window.blit(pause_text, (WINDOW_WIDTH-pause_text.get_width()-10, 10))
        window.blit(exit_text, (WINDOW_WIDTH-exit_text.get_width()-10, 50))
    else:
        # Display game over screen
        if level>5:
            if level>=10 and level<15:
                end_img = pygame.image.load(f"C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\end2.jpeg")
                game_over_text = font_exit.render(f"This isnt over yet! mate we need you", True, (255, 0, 255))
                game_over_image = pygame.transform.scale(end_img, (WINDOW_WIDTH,WINDOW_HEIGHT))
                window.blit(game_over_image, (0,0))
                window.blit(game_over_text, (50, WINDOW_HEIGHT-100))
                '''
            elif level>=15:
                end_img = pygame.image.load(f"C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\test_games\\end3.jpg")   
                game_over_text = font_exit.render(f"peace has been restored in the land ", True, (255, 0, 255))
                game_over_image = pygame.transform.scale(end_img, (WINDOW_WIDTH,WINDOW_HEIGHT))
                window.blit(game_over_image, (0,0))

                window.blit(game_over_text, (50, WINDOW_HEIGHT-100))'''
            else:
                end_img = pygame.image.load(f"C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\end1.jpeg")
                game_over_image = pygame.transform.scale(end_img, (WINDOW_WIDTH,WINDOW_HEIGHT))
                window.blit(game_over_image, (0,0))   
            game_over_text = font_exit.render(f"Game over checkpoint ending!press r to retry or press excape to exit", True, (255, 0, 255))
            window.blit(game_over_text, (50, WINDOW_HEIGHT-50))
        else:
            game_over_image = pygame.transform.scale(game_over_image, (WINDOW_WIDTH,WINDOW_HEIGHT))    
            game_over_text = font_exit.render(f"press enter or r to retry or press excape to exit", True, (255, 0, 255))
            window.blit(game_over_image, (0,0))
            window.blit(game_over_text, (50, WINDOW_HEIGHT-50))
            
        
                
    if show_popup:
        paused=True
        current_time = pygame.time.get_ticks()
        popup_elapsed = (current_time - popup_timer) / 1000  # Convert to seconds
        if popup_elapsed >= popup_duration:
            show_popup = False  # Hide the popup after the duration
            paused=False
            
        else:
            popup_text = popup_font.render(f"Level Up! Next Level starting increasing obstacle speed in {int(popup_duration-popup_elapsed)}", True, (255, 255, 255))
            popup_width = popup_text.get_width()
            popup_height = popup_text.get_height()
            popup_x = WINDOW_WIDTH // 2 - popup_width // 2
            popup_y = WINDOW_HEIGHT // 2 - popup_height // 2
            popup_rect = popup_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            pygame.draw.rect(window, (255, 0, 0), (150,300, WINDOW_WIDTH - 300, WINDOW_HEIGHT - 600))
            pygame.draw.rect(window, (255, 255, 255), (150, 300, WINDOW_WIDTH - 300, WINDOW_HEIGHT - 600), 3)
            window.blit(popup_text, popup_rect)
    

    if flag3:
        paused=True
        current_time = pygame.time.get_ticks()
        popup_elapsed = (current_time - popup_timer) / 1000  # Convert to seconds
        if popup_elapsed >= popup_duration and level<15:
            flag3 = False  # Hide the popup after the duration
            if level>=5:
                if level>=10 :
                    end_img = pygame.image.load(f"C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\end2.jpeg")
                    game_over_text = font_exit.render(f"This isnt over yet! mate we need you", True, (255, 0, 255))
                    game_over_image = pygame.transform.scale(end_img, (WINDOW_WIDTH,WINDOW_HEIGHT))
                    window.blit(game_over_image, (0,0))
                    window.blit(game_over_text, (50, WINDOW_HEIGHT-90))
                    
                else:
                    end_img = pygame.image.load(f"C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\end1.jpg")
                    game_over_image = pygame.transform.scale(end_img, (WINDOW_WIDTH,WINDOW_HEIGHT))
                    window.blit(game_over_image, (0,0))
            if popup_elapsed >= 10:
                running=False
        else:
            if level>=15:
                    end1=True
                    popup_text = popup_font.render(f"""All endings unlocked! You Won! press enter to play again or view ending and exit in {int(popup_duration-popup_elapsed)}""", True, (255, 255, 255))
                    popup_width = popup_text.get_width()
                    popup_height = popup_text.get_height()
                    popup_x = WINDOW_WIDTH // 2 - popup_width // 2
                    popup_y = WINDOW_HEIGHT // 2 - popup_height // 2
                    popup_rect = popup_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                    pygame.draw.rect(window, (255, 0, 0), (5,300, WINDOW_WIDTH - 10, WINDOW_HEIGHT - 600))
                    pygame.draw.rect(window, (255, 255, 255), (5, 300, WINDOW_WIDTH - 10, WINDOW_HEIGHT - 600), 3)
                    window.blit(popup_text, popup_rect)
                        
                    if popup_elapsed >= 5:
                        end_img = pygame.image.load(f"C:\\Users\\utkar\\OneDrive\\vscode\\py\\pyprojectmodule\\assets\\end3.jpg")   
                        game_over_text = font_exit.render(f"Peace has been restored in the land ", True, (255, 0, 255))
                        game_over_image = pygame.transform.scale(end_img, (WINDOW_WIDTH,WINDOW_HEIGHT))
                        window.blit(game_over_image, (0,0))
                        window.blit(game_over_text, (50, WINDOW_HEIGHT-90))
                    
                        if popup_elapsed>=10:
                            running=False
            else:    
                popup_text = popup_font.render(f"{end} ending unlocked press enter to continue playing or view ending and exit in {int(popup_duration-popup_elapsed)}", True, (255, 255, 255))
                popup_width = popup_text.get_width()
                popup_height = popup_text.get_height()
                popup_x = WINDOW_WIDTH // 2 - popup_width // 2
                popup_y = WINDOW_HEIGHT // 2 - popup_height // 2
                popup_rect = popup_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                pygame.draw.rect(window, (255, 0, 0), (30,300, WINDOW_WIDTH - 60, WINDOW_HEIGHT - 600))
                pygame.draw.rect(window, (255, 255, 255), (30, 300, WINDOW_WIDTH - 60, WINDOW_HEIGHT - 600), 3)
                window.blit(popup_text, popup_rect)
                if keys[pygame.K_RETURN] and flag3:
                    # Reset game
                    game_over = False
                    score = 0
                    level += 1
                    obstacle_speed-=2
                    max_score=10
                    max_level+=5
                    player_x = WINDOW_WIDTH // 2 - player_width // 2
                    obstacle_x = random.randint(player_x-300,player_x+300)
                    paused=False
                    flag3=False
                    show_popup=False        
    
    if obstacle_x<0:
        obstacle_x=0
    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
