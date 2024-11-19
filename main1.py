import pygame
from sprite import sprites, Sprite
from input import keys_down
from map import Map, TileKind
from player import Player
current_map_index = 0  # Start at the first map
# Player initialization
player = Player("images/player.png", 32 * 11, 32 * 7)
# Tile definitions
tile_kinds = [
        TileKind("dirt", "images/dirt.png", False),
        TileKind("grass", "images/grass.png", False),
        TileKind("water", "images/water.png", False),
        TileKind("wood", "images/wood.png", False)
    ]

# Map setup
map = Map("maps/start.map", tile_kinds, 32)

# Trigger areas for the initial map
trigger_areas = [
    {
        "x": 3, "y": 3,
        "message": "Found CeraVe Foaming Cleanser (Suitable for Oily Skin)!",
        "products": [{"image": "images/cerave1.png", "x": 100, "y": 100, "skin_type": "Oily"}]
    },
    {
        "x": 5, "y": 5,
        "message": "Found CeraVe Hydrating Facial Cleanser (Suitable for Dry Skin)!",
        "products": [{"image": "images/cerave2.png", "x": 200, "y": 200, "skin_type": "Dry"}]
    },
    {
        "x": 2, "y": 3,
        "message": "Found La Roche-Posay Toleriane Purifying Cleanser (Suitable for Combination Skin)!",
        "products": [{"image": "images/img3.png", "x": 300, "y": 300, "skin_type": "Combination"}]
    },
    {
        "x": 1, "y": 1,
        "message": "Found Vanicream Gentle Facial Cleanser (Suitable for Sensitive Skin)!",
        "products": [{"image": "images/img4.png", "x": 120, "y": 200, "skin_type": "Sensitive"}]
    }
]

# Trigger areas for the next map
next_map_trigger_areas = [
    {
        "x": 2, "y": 2,
        "message": "Found Paula's Choice Pore-Reducing Toner (Suitable for Oily Skin)!",
        "products": [{"image": "images/img5.png", "x": 120, "y": 120, "skin_type": "Oily"}]
    },
    {
        "x": 2, "y": 5,
        "message": "Found Klairs Supple Preparation Unscented Toner (Suitable for Dry Skin)!",
        "products": [{"image": "images/img6.png", "x": 200, "y": 150, "skin_type": "Dry"}]
    },
    {
        "x": 3, "y": 3,
        "message": "Found Laneige Cream Skin Toner & Moisturizer (Suitable for Combination Skin)!",
        "products": [{"image": "images/img7.png", "x": 200, "y": 180, "skin_type": "Combination"}]
    },
    {
        "x": 2, "y": 4,
        "message": "Found Avene Thermal Spring Water (Suitable for Sensitive Skin)!",
        "products": [{"image": "images/img8.png", "x": 100, "y": 140, "skin_type": "Sensitive"}]
    }
]

# Trigger areas for the third map
map3_trigger_areas = [
    {
        "x": 2, "y": 3,
        "message": "Found Neutrogena Hydro Boost Water Gel (Suitable for Oily Skin)!",
        "products": [{"image": "images/img9.png", "x": 100, "y": 100, "skin_type": "Oily"}]
    },
    {
        "x": 3, "y": 1,
        "message": "Found First Aid Beauty Ultra Repair Cream (Suitable for Dry Skin)!",
        "products": [{"image": "images/img10.png", "x": 200, "y": 200, "skin_type": "Dry"}]
    },
    {
        "x": 1, "y": 3,
        "message": "Found COSRX Oil-Free Ultra-Moisturizing Lotion (Suitable for Combination Skin)!",
        "products": [{"image": "images/img11.png", "x": 300, "y": 300, "skin_type": "Combination"}]
    },
    {
        "x": 2, "y": 2,
        "message": "Found Bioderma Sensibio AR Cream (Suitable for Sensitive Skin)!",
        "products": [{"image": "images/img12.png", "x": 300, "y": 300, "skin_type": "Sensitive"}]
    }
]

# Trigger areas for the fourth map
map4_trigger_areas = [
    {
        "x": 1, "y": 2,
        "message": "Found The Ordinary Niacinamide 10% + Zinc 1% (Suitable for Oily Skin)!",
        "products": [{"image": "images/img13.png", "x": 120, "y": 120, "skin_type": "Oily"}]
    },
    {
        "x": 1, "y": 3,
        "message": "Found Vichy Mineral 89 Hyaluronic Acid Serum (Suitable for Dry Skin)!",
        "products": [{"image": "images/img14.png", "x": 240, "y": 240, "skin_type": "Dry"}]
    },
    {
        "x": 2, "y": 2,
        "message": "Found Drunk Elephant C-Firma Fresh Vitamin C Serum (Suitable for Combination Skin)!",
        "products": [{"image": "images/img15.png", "x": 360, "y": 360, "skin_type": "Combination"}]
    },
    {
        "x": 3, "y": 2,
        "message": "Found Biore UV Aqua Rich Watery Essence SPF 50+ (Suitable for Sensitive Skin)!",
        "products": [{"image": "images/img16.png", "x": 360, "y": 360, "skin_type": "Sensitive"}]
    }
]

# Trigger areas for the fifth map
map5_trigger_areas = [
    {
        "x": 3, "y": 2,
        "message": "Found Neutrogena Ultra Sheer Dry-Touch SPF 55 (Suitable for Oily Skin)!",
        "products": [{"image": "images/img17.png", "x": 100, "y": 100, "skin_type": "Oily"}]
    },
    {
        "x": 2, "y": 4,
        "message": "Found La Roche-Posay Anthelios Melt-in Milk Sunscreen SPF 100 (Suitable for Dry Skin)!",
        "products": [{"image": "images/img18.png", "x": 100, "y": 100, "skin_type": "Dry"}]
    },
    {
        "x": 2, "y": 1,
        "message": "Found Dr. Jart+ Cicapair Tiger Grass Serum (Suitable for Combination Skin)!",
        "products": [{"image": "images/img19.png", "x": 100, "y": 100, "skin_type": "Combination"}]
    },
    {
        "x": 5, "y": 2,
        "message": "Found Blue Lizard Sensitive Mineral Sunscreen SPF 50 (Suitable for Sensitive Skin)!",
        "products": [{"image": "images/img20.png", "x": 360, "y": 360, "skin_type": "Sensitive"}]
    }
]

# Selected products
selected_product_1 = None
selected_product_2 = None

# Current map file and trigger areas
map_files = ["maps/start.map", "maps/next.map", "maps/map3.map", "maps/map4.map", "maps/map5.map"]
map_trigger_areas = [
    trigger_areas,
    next_map_trigger_areas,
    map3_trigger_areas,
    map4_trigger_areas,
    map5_trigger_areas
]

current_trigger_areas = trigger_areas  # Set initial trigger areas
selected_products = [None] * len(map_files)  # Track selected products for each map


def maze():
    Sprite("images/tree.png", 0 * 32, 0 * 32)


    Sprite("images/tree.png", 7 * 32, 2 * 32)
    Sprite("images/tree.png", 1 * 32, 10 * 32)
    Sprite("images/tree.png", 12 * 32, -1 * 32)
    Sprite("images/tree.png", 14 * 32, 9 * 32)
    Sprite("images/tree.png", 12 * 32, -1 * 32)
    Sprite("images/tree.png", 13 * 32, 12 * 32)
    Sprite("images/tree.png", 20 * 32, 9 * 32)
    Sprite("images/tree.png", 22 * 32, -1 * 32)
    Sprite("images/tree.png", 24 * 32, 12 * 32)
    Sprite("images/tree.png", 2 * 32, 8 * 32)
    Sprite("images/tree.png", 15 * 32, 15 * 32)
    Sprite("images/tree.png", 17 * 32, 1 * 32)
    Sprite("images/tree.png", 1 * 32, 15 * 32)

    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Adventure Game")
    screen = pygame.display.set_mode((800, 600))

    clear_color = (30, 150, 50)
    running = True

    # Update the load_next_map function
    def load_next_map():
        global current_map_index, map, current_trigger_areas, running
        if current_map_index + 1 < len(map_files):
            current_map_index += 1
            map.load_map(map_files[current_map_index])
            current_trigger_areas = map_trigger_areas[current_map_index]
            print(f"Switched to map {current_map_index + 1}")
        else:
            print("Reached the end of the maps!")
            setup_display_screen(selected_products)  # Show the shelf
            running = False  # End the game loop

    # Function to display the shelf with collected products
    def setup_display_screen(selected_products):
        pygame.init()
        screen_width, screen_height = 900, 700
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Skincare Shelf Display")

        # Load background
        background = Background(screen, "assets/background.jpg")

        # Load shelf
        shelf = Shelf(screen, "assets/shelf.png", position=((screen_width - 700) // 2, 380))

        # Prepare products for display and initialize skin type scores
        products = []
        skin_type_scores = {"Oily": 0, "Dry": 0, "Combination": 0, "Sensitive": 0}  # Track scores dynamically
        x_offset = (screen_width - 700) // 2 + 20

        for i, product in enumerate(selected_products):
            if product:  # Only add selected products
                position = (x_offset + i * 140, 280)
                products.append(SkincareProduct(
                    screen,
                    product["image"],
                    position, # Extract product name
                    {"Oily": 1 if product["skin_type"] == "Oily" else 0,
                     "Dry": 1 if product["skin_type"] == "Dry" else 0,
                     "Combination": 1 if product["skin_type"] == "Combination" else 0,
                     "Sensitive": 1 if product["skin_type"] == "Sensitive" else 0},
                ))
                # Update scores dynamically
                skin_type_scores[product["skin_type"]] += 1

        # Determine the best skin type based on scores
        best_fit_skin_type = max(skin_type_scores, key=skin_type_scores.get)
        conclusion_text = f"The selected products are best suited for {best_fit_skin_type} skin."

        # Recommendations based on the best-fit skin type
        recommendations = {
            "Oily": "Use lightweight, oil-free moisturizers. Avoid heavy creams. Look for products with salicylic acid or niacinamide to control oil.",
            "Dry": "Hydrate your skin with rich creams and moisturizers. Use products with hyaluronic acid and glycerin for long-lasting hydration.",
            "Combination": "Balance hydration and oil control. Use lightweight moisturizers in oily areas and richer creams on dry areas.",
            "Sensitive": "Opt for fragrance-free, hypoallergenic products. Look for soothing ingredients like aloe vera or chamomile."
        }
        recommendation_text = recommendations.get(best_fit_skin_type, "Keep your skin healthy with a balanced routine.")

        # Display loop
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update hover states for products
            for product in products:
                product.check_hover(mouse_pos)

            # Display everything
            background.display()
            shelf.display()
            for product in products:
                product.display()


            font = pygame.font.Font(None, 24)
            general_text = "Here results of this game and some recommendations for you!"
            general_text_surface = font.render(general_text, True, (0, 0, 0))
            general_text_rect = general_text_surface.get_rect(center=(screen_width // 2, 50))
            screen.blit(general_text_surface, general_text_rect)

            # Display the conclusion
            conclusion_surface = font.render(conclusion_text, True, (0, 0, 0))
            conclusion_rect = conclusion_surface.get_rect(center=(screen_width // 2, 600))
            screen.blit(conclusion_surface, conclusion_rect)

            # Display recommendations
            recommendation_surface = font.render(recommendation_text, True, (0, 0, 0))
            recommendation_rect = recommendation_surface.get_rect(center=(screen_width // 2, 650))
            screen.blit(recommendation_surface, recommendation_rect)

            pygame.display.update()

        pygame.quit()

    def check_triggers(self):
        # Calculate the player's tile position
        tile_x = self.x // 32
        tile_y = self.y // 32

        # Check if the player's position matches any trigger area in current_trigger_areas
        for area in current_trigger_areas:
            if area["x"] == tile_x and area["y"] == tile_y:
                if self.message != area["message"]:  # Only set a new message
                    self.message = area["message"]
                    self.message_timer = 120  # Display message for 2 seconds (120 frames at 60 FPS)

                    # Trigger product dialog
                    for product in area["products"]:
                        self.dialog_product = product
                return

        # Draw the dialog


    def draw_dialog(screen, product):
        dialog_rect = pygame.Rect(200, 150, 400, 200)
        pygame.draw.rect(screen, (0, 0, 0), dialog_rect)
        pygame.draw.rect(screen, (255, 255, 255), dialog_rect, 3)

        font = pygame.font.Font(None, 36)
        text_surface = font.render("Do you want to take it?", True, (255, 255, 255))
        screen.blit(text_surface, (dialog_rect.x + 50, dialog_rect.y + 30))

        yes_button = pygame.Rect(dialog_rect.x + 50, dialog_rect.y + 100, 100, 50)
        no_button = pygame.Rect(dialog_rect.x + 250, dialog_rect.y + 100, 100, 50)

        pygame.draw.rect(screen, (0, 255, 0), yes_button)
        pygame.draw.rect(screen, (255, 0, 0), no_button)

        yes_text = font.render("Yes", True, (0, 0, 0))
        no_text = font.render("No", True, (0, 0, 0))
        screen.blit(yes_text, (yes_button.x + 25, yes_button.y + 10))
        screen.blit(no_text, (no_button.x + 25, no_button.y + 10))

        return yes_button, no_button

        # Draw selected products


    def draw_selected_products(screen, selected_products):
        for i, product in enumerate(selected_products):
            if product:
                product_image = pygame.image.load(product["image"])
                x_offset = 50 + i * 100  # Space products horizontally
                y_position = screen.get_height() - 50  # Position at the bottom
                product_rect = product_image.get_rect(bottomleft=(x_offset, y_position))
                screen.blit(product_image, product_rect)

        # Main game loop


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys_down.add(event.key)
            elif event.type == pygame.KEYUP:
                keys_down.remove(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if player.dialog_product:
                    yes_button, no_button = draw_dialog(screen, player.dialog_product)
                    if yes_button.collidepoint(mouse_pos):
                        if current_map_index < len(selected_products):
                            selected_products[current_map_index] = player.dialog_product
                            print(f"Selected product for map {current_map_index + 1}: {player.dialog_product}")
                        player.dialog_product = None
                    elif no_button.collidepoint(mouse_pos):
                        player.dialog_product = None

        # Update player and triggers
        player.update()
        player.check_triggers(current_trigger_areas)  # Pass the current trigger areas dynamically

        # Bottom-right threshold
        if player.x >= screen.get_width() - 200 and player.y >= screen.get_height() - 200:
            if selected_products[current_map_index] is not None:  # Check if a product has been selected
                load_next_map()
            else:
                print("You must select a product before moving to the next map!")

        # Draw everything
        screen.fill(clear_color)
        map.draw(screen)

        for s in sprites:
            s.draw(screen)

        if player.dialog_product:
            draw_dialog(screen, player.dialog_product)

        draw_selected_products(screen, selected_products)

        # Draw the player's message if it exists
        if player.message:
            font = pygame.font.Font(None, 24)
            text_surface = font.render(player.message, True, (255, 255, 255))
            screen.blit(text_surface, (player.x, player.y - 40))  # Display above the player

        # Cap the frames
        pygame.time.delay(17)
        pygame.display.flip()

    pygame.quit()


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
    def __init__(self, screen, image_path, position,  skin_type_scores, size_multiplier=1.5):
        self.screen = screen
        self.image_path = image_path
        self.original_image = pygame.image.load(image_path)
        # Scale the image to a larger size using the size multiplier
        self.size = (int(self.original_image.get_width() * size_multiplier),
                     int(self.original_image.get_height() * size_multiplier))
        self.image = pygame.transform.scale(self.original_image, self.size)  # Enlarge the image
        self.position = position  # Position where the product will be displayed
        self.skin_type_scores = skin_type_scores  # Ratings for skin types
        self.font = pygame.font.Font(None, 24)
        self.text_color = (0, 0, 0)  # Black color for the text
        self.hovered = False

    def display(self):
        # Display the product image
        if self.hovered:
            # If hovered, display a slightly larger image
            enlarged_image = pygame.transform.scale(
                self.original_image,
                (int(self.size[0] * 1.1), int(self.size[1] * 1.1))
            )
            enlarged_rect = enlarged_image.get_rect(center=(self.position[0] + self.size[0] // 2,
                                                             self.position[1] + self.size[1] // 2))
            self.screen.blit(enlarged_image, enlarged_rect.topleft)
        else:
            self.screen.blit(self.image, self.position)


    def check_hover(self, mouse_pos):
        # Check if the mouse is hovering over the product
        rect = pygame.Rect(self.position[0], self.position[1], *self.size)
        self.hovered = rect.collidepoint(mouse_pos)

