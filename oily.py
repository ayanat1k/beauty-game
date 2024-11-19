# oily.py
import pygame

class OilySkin:
    def __init__(self):
        # Define the steps for the oily skin routine
        self.routine_steps = [
            "Step 1: Gel-Based Cleanser – A gentle gel cleanser removes excess oil without stripping the skin.",
            "Step 2: Exfoliating Toner – A toner with salicylic acid can help reduce oil and prevent clogged pores.",
            "Step 3: Niacinamide Serum – Niacinamide regulates oil production and reduces pore size.",
            "Step 4: Lightweight Moisturizer – Opt for an oil-free, gel moisturizer to hydrate without clogging pores.",
            "Step 5: Sunscreen – Use a mattifying, oil-free SPF to protect your skin without adding shine."
        ]

    def display_routine(self, screen, font, colors):
        small_font = pygame.font.Font(None, 28)  # Set a smaller font size
        screen.fill(colors["WHITE"])  # Clear the screen with white background
        title_text = small_font.render("Oily Skin Routine", True, colors["BLUE"])
        screen.blit(title_text, (50, 50))  # Display the title

        # Display each step of the routine
        for i, step in enumerate(self.routine_steps):
            step_text = small_font.render(step, True, colors["BLACK"])
            screen.blit(step_text, (50, 100 + i * 40))  # Adjust Y position for each step
        pygame.display.update()