# combination.py
import pygame

class CombinationSkin:
    def __init__(self):
        self.steps = [
            "1. Foaming Cleanser: A foaming cleanser can address oil in the T-zone while being gentle on dry areas.",
            "2. Pore-Tightening Toner: Use a toner that targets oily areas without over-drying other parts of the face.",
            "3. Hydrating Serum: Apply a hydrating serum with hyaluronic acid, focusing on the dry areas.",
            "4. Light Gel Moisturizer: Use a gel moisturizer that hydrates without adding too much oil.",
            "5. SPF with a Matte Finish: Apply a lightweight, mattifying sunscreen to control shine in the T-zone."
        ]

    def display_routine(self, screen, font, colors):
        small_font = pygame.font.Font(None, 28)  # Smaller font size
        screen.fill(colors["WHITE"])
        title_text = small_font.render("Combination Skin Routine", True, colors["BLUE"])
        screen.blit(title_text, (50, 50))

        for i, step in enumerate(self.steps):
            step_text = small_font.render(step, True, colors["BLACK"])
            screen.blit(step_text, (50, 100 + i * 40))
        pygame.display.update()