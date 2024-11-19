# normal.py
import pygame

class NormalSkin:
    def __init__(self):
        self.steps = [
            "1. Gentle Cleanser: A mild, foaming cleanser maintains a balanced complexion.",
            "2. Balancing Toner: Use a toner with antioxidants to keep the skin radiant and balanced.",
            "3. Vitamin C Serum: Apply a Vitamin C serum to boost radiance and prevent environmental damage.",
            "4. Light Moisturizer: A lightweight cream keeps the skin hydrated without being heavy.",
            "5. Broad-Spectrum SPF: Apply sunscreen to protect your skin from UV damage."
        ]

    def display_routine(self, screen, font, colors):
        small_font = pygame.font.Font(None, 28)  # Smaller font size
        screen.fill(colors["WHITE"])
        title_text = small_font.render("Normal Skin Routine", True, colors["BLUE"])
        screen.blit(title_text, (50, 50))

        for i, step in enumerate(self.steps):
            step_text = small_font.render(step, True, colors["BLACK"])
            screen.blit(step_text, (50, 100 + i * 40))
        pygame.display.update()