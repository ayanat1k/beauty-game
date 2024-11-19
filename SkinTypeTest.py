import pygame

class SkinTypeTest:
    def __init__(self, screen, font, colors, screen_width, screen_height):
        self.screen = screen
        self.font = font
        self.colors = colors
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Initialize attributes
        self.questions = [
            "How does your skin feel throughout the day?",
            "How often do you get pimples or breakouts?",
            "How does your skin react to skincare products?",
            "How are your pores?",
            "How does your skin look like?"  # New image-based question
        ]
        self.options = [
            ["a) Always dry and tight", "b) Comfortable without needing extra care", "c) Oily in the T-zone",
             "d) Shiny all over the face"],
            ["a) Rarely or never", "b) Occasionally, but disappear quickly", "c) Sometimes in T-zone",
             "d) Frequently on different areas"],
            ["a) Often irritated or red", "b) No reaction, skin stays fine", "c) Feels oily after creams",
             "d) Absorbs quickly, shines soon after"],
            ["a) Almost invisible", "b) Slightly visible up close", "c) Enlarged in T-zone",
             "d) Large and visible across the face"],
            []  # Placeholder for image-based options
        ]
        self.answers = []
        self.current_question = 0
        self.answer_rects = []
        self.image_size = (250, 250)

        # Load images for the image-based question
        self.image_options = [
            pygame.transform.scale(pygame.image.load('dry.png'), self.image_size),  # Replace with actual image paths
            pygame.transform.scale(pygame.image.load('normal.png'), self.image_size),
            pygame.transform.scale(pygame.image.load('comb.png'), self.image_size),
            pygame.transform.scale(pygame.image.load('oily.png'), self.image_size)
        ]
        self.image_coords = [
            (self.screen_width // 4 - self.image_size[0] // 2, 100),  # Column 1, Row 1
            (3 * self.screen_width // 4 - self.image_size[0] // 2, 100),  # Column 2, Row 1
            (self.screen_width // 4 - self.image_size[0] // 2, 400),  # Column 1, Row 2
            (3 * self.screen_width // 4 - self.image_size[0] // 2, 400)  # Column 2, Row 2
        ]
        # Load the arrow button for navigating back
        self.arrow_button = pygame.image.load('arrow-button.png')
        self.arrow_button = pygame.transform.scale(self.arrow_button, (50, 50))
        self.arrow_button_rect = self.arrow_button.get_rect(center=(100, screen_height // 2))
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound('click.wav')  # Звук клика

    def display_question(self):
        self.screen.fill(self.colors["WHITE"])
        question_text = self.font.render(self.questions[self.current_question], True, self.colors["BLUE"])
        self.screen.blit(question_text, (self.screen_width // 2 - question_text.get_width() // 2, 50))
        self.answer_rects.clear()  # Clear previous rects

        if self.current_question < len(self.questions) - 1:  # Text-based questions
            for i, option_text in enumerate(self.options[self.current_question]):
                option_surface = self.font.render(option_text, True, self.colors["BLACK"])
                option_rect = option_surface.get_rect(center=(self.screen_width // 2, 150 + i * 60))
                pygame.draw.rect(self.screen, self.colors["BLUE"],
                                 option_rect.inflate(20, 10))  # Draw background for option
                self.screen.blit(option_surface, option_rect)
                self.answer_rects.append((option_text[0].lower(), option_rect))  # Store answer letter and rect
        else:  # Image-based question
            for i, (image, coord) in enumerate(zip(self.image_options, self.image_coords)):
                self.screen.blit(image, coord)  # Display image
                rect = pygame.Rect(coord[0], coord[1], 250, 250)  # Define click area for the image
                pygame.draw.rect(self.screen, self.colors["GRAY"], rect, 2)  # Add border
                self.answer_rects.append((chr(97 + i), rect))  # Map 'a', 'b', 'c', 'd' to images

        # Draw the arrow button
        self.screen.blit(self.arrow_button, self.arrow_button_rect)

    def handle_click(self, pos):
        for answer, rect in self.answer_rects:
            if rect.collidepoint(pos):
                self.answers.append(answer)
                self.current_question += 1

                self.click_sound.play()

                if self.current_question >= len(self.questions):
                    return "results"  # Navigate to results
                break
        if self.arrow_button_rect.collidepoint(pos):
            self.click_sound.play()
            return "options"  # Navigate back to options

    def calculate_skin_type(self):
        # Count the occurrences of each answer type
        a_count = self.answers.count('a')
        b_count = self.answers.count('b')
        c_count = self.answers.count('c')
        d_count = self.answers.count('d')

        # Determine skin type based on most frequent answer
        if a_count > max(b_count, c_count, d_count):
            return "Dry Skin"
        elif b_count > max(a_count, c_count, d_count):
            return "Normal Skin"
        elif c_count > max(a_count, b_count, d_count):
            return "Combination Skin"
        elif d_count > max(a_count, b_count, c_count):
            return "Oily Skin"
