import pygame

from sprite import Sprite
from input import is_key_pressed

movement_speed = 2

# Trigger areas for the initial map
trigger_areas = [
    {
        "x": 3, "y": 3,
        "message": "Found CeraVe Foaming Cleanser!",
        "products": [{"image": "images/im.png", "x": 100, "y": 100}]
    },
    {
        "x": 5, "y": 5,
        "message": "Found CeraVe Hydrating Facial Cleanser!",
        "products": [{"image": "images/im.png", "x": 200, "y": 200}]
    },
    {
        "x": 8, "y": 8,
        "message": "Found La Roche-Posay Toleriane Purifying Cleanser!",
        "products": [{"image": "images/im.png", "x": 300, "y": 300}]
    },
    {
        "x": 1, "y": 4,
        "message": "Found Vanicream Gentle Facial Cleanser!",
        "products": [{"image": "images/im.png", "x": 400, "y": 400}]
    }
]

# Trigger areas for the next map
next_map_trigger_areas = [
    {
        "x": 4, "y": 2,
        "message": "Found Neutrogena Hydro Boost Gel-Cream!",
        "products": [{"image": "images/img1.png", "x": 120, "y": 120}]
    },
    {
        "x": 6, "y": 6,
        "message": "Found Cetaphil Gentle Skin Cleanser!",
        "products": [{"image": "images/img1.png", "x": 240, "y": 240}]
    },
    {
        "x": 9, "y": 5,
        "message": "Found First Aid Beauty Pure Skin Cleanser!",
        "products": [{"image": "images/img1.png", "x": 360, "y": 360}]
    },
    {
        "x": 2, "y": 7,
        "message": "Found Bioderma Sensibio H2O Micellar Water!",
        "products": [{"image": "images/img1.png", "x": 480, "y": 480}]
    }
]


class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.message = ""  # Current message
        self.message_timer = 0  # Timer for how long the message stays visible
        self.dialog_product = None  # Product being interacted with

    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= movement_speed
        if is_key_pressed(pygame.K_s):
            self.y += movement_speed
        if is_key_pressed(pygame.K_a):
            self.x -= movement_speed
        if is_key_pressed(pygame.K_d):
            self.x += movement_speed

        # Decrease message timer
        if self.message_timer > 0:
            self.message_timer -= 1
        else:
            self.message = ""  # Clear the message when timer runs out

    def check_triggers(self, trigger_areas):
        # Calculate the player's tile position
        tile_x = self.x // 32
        tile_y = self.y // 32

        # Dynamically check against the provided trigger areas
        for area in trigger_areas:
            if area["x"] == tile_x and area["y"] == tile_y:
                if self.message != area["message"]:  # Only set a new message
                    self.message = area["message"]
                    self.message_timer = 120  # Display message for 2 seconds (120 frames at 60 FPS)

                    # Trigger product dialog
                    for product in area["products"]:
                        self.dialog_product = product
                return



