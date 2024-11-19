import pygame
import sys
import sqlite3  # For database
from SkinTypeTest import SkinTypeTest  # Import SkinTypeTest
from oily import OilySkin  # Import OilySkin
from dry import DrySkin  # Import DrySkin
from combination import CombinationSkin  # Import CombinationSkin
from normal import NormalSkin  # Import NormalSkin
from display_shelf import setup_display  # Import shelf display function
from main1 import maze

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Your Beauty Assist")

# Colors


colors = {
    "WHITE": (255, 255, 255),
    "BLUE": (70, 130, 180),
    "PINK": (255, 192, 203),
    "LIGHT_PINK": (255, 182, 193),
    "LAVENDER": (230, 230, 250),
    "PEACH": (255, 218, 185),
    "SOFT_BLUE": (173, 216, 230),
    "GRAY": (200, 200, 200),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (144, 238, 144),
}
WHITE = colors["WHITE"]
PINK = colors["PINK"]
LIGHT_PINK = colors["LIGHT_PINK"]
LAVENDER = colors["LAVENDER"]
PEACH = colors["PEACH"]
SOFT_BLUE = colors["SOFT_BLUE"]
GRAY = colors["GRAY"]
BLACK = colors["BLACK"]
RED = colors["RED"]
GREEN = colors["GREEN"]
BLUE = colors["BLUE"]

# Load assets
icon = pygame.image.load('beauty-and-cosmetics.png')
pygame.display.set_icon(icon)

background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

start_button = pygame.image.load('start-button.png')
start_button = pygame.transform.scale(start_button, (250, 200))
start_button_rect = start_button.get_rect(center=(screen_width // 2, screen_height // 2 - 50))

# Load arrow button for "Next" step
arrow_button = pygame.image.load('arrow-button.png')
arrow_button = pygame.transform.scale(arrow_button, (50, 50))
arrow_button_rect = arrow_button.get_rect(center=(screen_width // 2, screen_height // 2 + 100))

# Font
title_font = pygame.font.Font(None, 64)
font = pygame.font.Font(None, 36)

# Options for skin types including "Take a Test"
options = ["Take a Test", "Play", "Music On/Off", "Exit"]
button_rects = []  # Store button rects

# Music variables
pygame.mixer.music.load('music.mp3')  # Replace with your music file
pygame.mixer.music.set_volume(0.5)
music_playing = True  # Track whether music is playing

# Start music playback
pygame.mixer.music.play(-1)  # Loop indefinitely

# Function to toggle music
def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    music_playing = not music_playing

pygame.mixer.init()
click_sound = pygame.mixer.Sound('click.wav')

# Create button rectangles for options screen
button_width, button_height = 250, 50
start_y = screen_height // 2 - 150
for i, option in enumerate(options):
    button_rect = pygame.Rect(
        screen_width // 2 - button_width // 2,
        start_y + i * (button_height + 15),
        button_width,
        button_height
    )
    button_rects.append((option, button_rect))

# Game state variable
game_state = "start"

# Create an instance of SkinTypeTest with the necessary arguments
skin_test = SkinTypeTest(screen, font, colors, screen_width, screen_height)

# Instances for skin type classes
oily_skin = OilySkin()
dry_skin = DrySkin()
normal_skin = NormalSkin()
combination_skin = CombinationSkin()


# Function to display the start screen
def display_start_screen():
    screen.blit(background_image, (0, 0))
    screen.blit(start_button, start_button_rect)
    title_text = title_font.render("Your Skincare Assist", True, (255, 255, 255))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 2 - 300))


# Function to display the options screen
def display_options_screen():
    screen.blit(background_image, (0, 0))
    title_text = font.render("Determine your face type and then in the game choose your products", True, WHITE)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

    # Draw buttons for each option
    for option, button_rect in button_rects:
        pygame.draw.rect(screen, BLUE, button_rect)
        option_text = font.render(option, True, WHITE)
        screen.blit(option_text, (
        button_rect.centerx - option_text.get_width() // 2, button_rect.centery - option_text.get_height() // 2))


# Function to display the test result and "Next" button
def display_test_result(skin_type):
    screen.fill(WHITE)
    result_text = f"Your skin type is: {skin_type}"
    text = font.render(result_text, True, BLUE)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2))
    screen.blit(arrow_button, arrow_button_rect)  # Display the arrow button


# Font
title_font = pygame.font.Font(None, 64)
font = pygame.font.Font(None, 36)

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

# Game state variable
game_state = "login"
error_message = ""
success_message = ""

# Input fields for login and registration
username = ""
password = ""
active_field = "username"  # Track which input field is active


# Function to display the login screen
# Function to draw rounded rectangles
def draw_rounded_rect(surface, rect, color, radius=20):
    pygame.draw.rect(surface, color, rect, border_radius=radius)


# Login Screen Design
def display_login_screen():
    # Background color for the login screen
    screen.fill(LAVENDER)  # Lavender for a soft, girly background

    # Title text
    title_text = title_font.render("Welcome Back, Sweetie!", True, BLACK)  # Pink text for the title
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

    # Text and positioning
    text = "Get ready to discover your perfect skincare routine!"
    x = screen_width // 2 - font.size(text)[0] // 2  # Center horizontally
    y = 120  # Position vertically

    # Render the text with the border (black color)
    border_color = BLACK
    text_surface = font.render(text, True, border_color)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
        screen.blit(text_surface, (x + dx, y + dy))

    # Render the main text (white color)
    text_color = WHITE
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (x, y))

    # Username field label and input box
    username_text = font.render("Username:", True, BLACK)
    screen.blit(username_text, (200, 250))
    draw_rounded_rect(screen, (400, 250, 300, 40),
                      LIGHT_PINK if active_field == "username" else WHITE)  # Pink outline if active
    username_display = font.render(username, True, BLACK)
    screen.blit(username_display, (410, 260))

    # Password field label and input box
    password_text = font.render("Password:", True, BLACK)
    screen.blit(password_text, (200, 350))
    draw_rounded_rect(screen, (400, 350, 300, 40),
                      LIGHT_PINK if active_field == "password" else WHITE)  # Pink outline if active
    password_display = font.render("*" * len(password), True, BLACK)
    screen.blit(password_display, (410, 360))

    # Login button
    login_button = pygame.Rect(200, 450, 200, 50)
    draw_rounded_rect(screen, login_button, SOFT_BLUE)  # Soft blue button
    login_text = font.render("Login", True, WHITE)
    screen.blit(login_text, (
    login_button.centerx - login_text.get_width() // 2, login_button.centery - login_text.get_height() // 2))

    # Register button
    register_button = pygame.Rect(500, 450, 200, 50)
    draw_rounded_rect(screen, register_button, PINK)  # Pink button
    register_text = font.render("Register", True, WHITE)
    screen.blit(register_text, (register_button.centerx - register_text.get_width() // 2,
                                register_button.centery - register_text.get_height() // 2))

    # Error message display
    if error_message:
        error_text = font.render(error_message, True, RED)
        screen.blit(error_text, (screen_width // 2 - error_text.get_width() // 2, 520))


# Function to display the registration screen
def display_register_screen():
    screen.fill(WHITE)
    title_text = title_font.render("Register an Account", True, PEACH)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))

    # Username field
    username_text = font.render("Username:", True, BLACK)
    screen.blit(username_text, (200, 250))
    pygame.draw.rect(screen, GRAY if active_field == "username" else WHITE, (400, 250, 300, 40))
    username_display = font.render(username, True, BLACK)
    screen.blit(username_display, (410, 260))

    # Password field
    password_text = font.render("Password:", True, BLACK)
    screen.blit(password_text, (200, 350))
    pygame.draw.rect(screen, GRAY if active_field == "password" else WHITE, (400, 350, 300, 40))
    password_display = font.render("*" * len(password), True, BLACK)
    screen.blit(password_display, (410, 360))

    # Register button
    register_button = pygame.Rect(350, 450, 200, 50)
    pygame.draw.rect(screen, PEACH, register_button)
    register_text = font.render("Register", True, WHITE)
    screen.blit(register_text, (register_button.centerx - register_text.get_width() // 2,
                                register_button.centery - register_text.get_height() // 2))

    # Display error or success message
    if error_message:
        error_text = font.render(error_message, True, RED)
        screen.blit(error_text, (screen_width // 2 - error_text.get_width() // 2, 520))
    if success_message:
        success_text = font.render(success_message, True, PEACH)
        screen.blit(success_text, (screen_width // 2 - success_text.get_width() // 2, 520))


# Function to validate login credentials
def validate_login(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone() is not None


# Function to register a new user
def register_user(username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif game_state == "login":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detect login button
                if 200 <= event.pos[0] <= 400 and 450 <= event.pos[1] <= 500:
                    click_sound.play()
                    if validate_login(username, password):
                        game_state = "start"  # Proceed to the game
                        error_message = ""
                        success_message = ""
                    else:
                        error_message = "Invalid username or password!"
                        success_message = ""
                # Detect register button
                elif 500 <= event.pos[0] <= 700 and 450 <= event.pos[1] <= 500:
                    click_sound.play()
                    game_state = "register"  # Switch to registration screen
                    username = ""
                    password = ""
                    active_field = "username"  # Reset active field
                    error_message = ""
                    success_message = ""
                # Detect active input field
                elif 400 <= event.pos[0] <= 700 and 250 <= event.pos[1] <= 290:
                    click_sound.play()
                    active_field = "username"
                elif 400 <= event.pos[0] <= 700 and 350 <= event.pos[1] <= 390:
                    click_sound.play()
                    active_field = "password"
            elif event.type == pygame.KEYDOWN:
                # Update active field
                if active_field == "username":
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_field == "password":
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
        elif game_state == "register":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detect register button
                if 350 <= event.pos[0] <= 550 and 450 <= event.pos[1] <= 500:
                    click_sound.play()
                    if username and password:
                        if register_user(username, password):
                            success_message = "Registration successful!"
                            error_message = ""
                            game_state = "start"  # Go directly to the game
                        else:
                            error_message = "Username already exists!"
                            success_message = ""
                    else:
                        error_message = "Username and password cannot be empty!"
                # Detect active input field
                elif 400 <= event.pos[0] <= 700 and 250 <= event.pos[1] <= 290:
                    click_sound.play()
                    active_field = "username"
                elif 400 <= event.pos[0] <= 700 and 350 <= event.pos[1] <= 390:
                    click_sound.play()
                    active_field = "password"
            elif event.type == pygame.KEYDOWN:
                # Update active field
                if active_field == "username":
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_field == "password":
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

    # Display screens based on game state
    if game_state == "login":
        display_login_screen()
    elif game_state == "register":
        display_register_screen()
    elif game_state == "start":
        display_start_screen()  # Transition to your game's start screen

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if game_state == "start" and start_button_rect.collidepoint(event.pos):
                        click_sound.play()
                        game_state = "options"  # Go to options screen on start button click
                    elif game_state == "options":
                        for option, button_rect in button_rects:
                            if button_rect.collidepoint(event.pos):
                                click_sound.play()
                                if option == "Play":
                                    maze()
                                elif option == "Take a Test":
                                    game_state = "test"
                                elif option == "Music On/Off":
                                    toggle_music()  # Toggle background music


                    elif game_state == "test":
                        result = skin_test.handle_click(event.pos)
                        if result == "options":
                            click_sound.play()
                            game_state = "options"
                        elif result == "results":
                            click_sound.play()
                            skin_type = skin_test.calculate_skin_type() or "Normal Skin"
                            game_state = "show_result"
                    elif game_state == "show_result" and arrow_button_rect.collidepoint(event.pos):
                        click_sound.play()
                        setup_display(skin_type)  # Open the shelf display with products
                        game_state = "options"  # Return to options after viewing the shelf

            # Display the current screen based on the game state
            if game_state == "start":
                display_start_screen()
            elif game_state == "options":
                display_options_screen()
            elif game_state == "test":
                skin_test.display_question()
            elif game_state == "show_result":
                display_test_result(skin_type)

            pygame.display.update()

    pygame.display.update()

# Close database connection and quit
conn.close()
pygame.quit()
sys.exit()
