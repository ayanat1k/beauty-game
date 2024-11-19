import pygame
import sys


class Background:
    def __init__(self, screen, image_path):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (screen.get_width(), screen.get_height()))

    def display(self):
        self.screen.blit(self.image, (0, 0))


class Shelf:
    def __init__(self, screen, image_path, position, size=(700, 200)):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.position = position


    def display(self):
        self.screen.blit(self.image, self.position)


class SkincareProduct:
    def __init__(self, screen, image_path, position, text, size=(80, 150)):
        self.screen = screen
        self.image_path = image_path
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, size)
        self.position = position
        self.size = size
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.text_color = (139, 69, 19)  # Коричневый цвет текста
        self.hovered = False

    def display(self):
        # Обновление изображения при наведении
        if self.hovered:
            enlarged_image = pygame.transform.scale(self.original_image, (int(self.size[0] * 1.1), int(self.size[1] * 1.1)))
            enlarged_rect = enlarged_image.get_rect(center=(self.position[0] + self.size[0] // 2, self.position[1] + self.size[1] // 2))
            self.screen.blit(enlarged_image, enlarged_rect.topleft)
        else:
            self.screen.blit(self.image, self.position)

        # Разделение текста на строки
        words = self.text.split()
        for i, word in enumerate(words):
            text_surface = self.font.render(word, True, self.text_color)
            text_rect = text_surface.get_rect(center=(self.position[0] + self.size[0] // 2, self.position[1] + self.size[1] + 10 + i * 20))
            self.screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        # Проверка на наведение
        rect = pygame.Rect(self.position[0], self.position[1], *self.size)
        self.hovered = rect.collidepoint(mouse_pos)

def setup_display(skin_type):
    pygame.init()
    pygame.font.init()

    font = pygame.font.Font(None, 36)
    screen_width, screen_height = 900, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Skincare Shelf Display")

    # Load background and shelf
    background = Background(screen, "assets/background.png")
    shelf = Shelf(screen, "assets/shelf.png", position=((screen_width - 700) // 2, 380))
    info_text = "You can play a game and determine what products fit you more."
    title_font = pygame.font.Font(None, 36)
    text_surface = title_font.render(info_text, True, (0, 0, 0))  # Black text color
    screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, 50))  # Centered at the top
    pygame.display.update()
    # Define products for the selected skin type
    product_data = {
        "Oily Skin": [
            ("assets/cleanser.png", "Gel-Based Cleanser"),
            ("assets/toner.png", "Exfoliating Toner"),
            ("assets/serum.png", "Niacinamide Serum"),
            ("assets/moisturizer.png", "Lightweight Moisturizer"),
            ("assets/sunscreen.png", "Sunscreen")
        ],
        "Dry Skin": [
            ("assets/cleanser.png", "Cream Cleanser"),
            ("assets/toner.png", "Hydrating Toner"),
            ("assets/serum.png", "Hyaluronic Acid Serum"),
            ("assets/moisturizer.png", "Rich Moisturizer"),
            ("assets/sunscreen.png", "Moisturizing SPF")
        ],
        "Normal Skin": [
            ("assets/cleanser.png", "Gentle Cleanser"),
            ("assets/toner.png", "Balancing Toner"),
            ("assets/serum.png", "Vitamin C Serum"),
            ("assets/moisturizer.png", "Light Moisturizer"),
            ("assets/sunscreen.png", "Broad-Spectrum SPF")
        ],
        "Combination Skin": [
            ("assets/cleanser.png", "Foaming Cleanser"),
            ("assets/toner.png", "Pore-Tightening Toner"),
            ("assets/serum.png", "Hydrating Serum"),
            ("assets/moisturizer.png", "Light Gel Moisturizer"),
            ("assets/sunscreen.png", "SPF with a Matte Finish")
        ]
    }

    # Load products for the selected skin type
    products = []
    x_offset = (screen_width - 700) // 2 + 20
    for i, (img_path, text) in enumerate(product_data[skin_type]):
        position = (x_offset + i * 140, 280)
        products.append(SkincareProduct(screen, img_path, position, text))

    # Draw the "Go Back to Menu" button
    def draw_back_to_menu_button():
        back_button_rect = pygame.Rect(20, screen_height - 60, 200, 50)  # Bottom-left corner
        pygame.draw.rect(screen, (255, 192, 203), back_button_rect, border_radius=10)
        back_text = font.render("Go Back to Menu", True, (255, 255, 255))
        screen.blit(back_text, (
            back_button_rect.centerx - back_text.get_width() // 2,
            back_button_rect.centery - back_text.get_height() // 2
        ))
        return back_button_rect

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(mouse_pos):  # Check if "Go Back" button is clicked
                    return  # Exit the shelf display and return to the main menu

        # Check hover state for each product
        for product in products:
            product.check_hover(mouse_pos)

        # Display everything
        background.display()
        shelf.display()
        for product in products:
            product.display()
        back_button_rect = draw_back_to_menu_button()  # Draw the "Go Back" button

        pygame.display.update()

