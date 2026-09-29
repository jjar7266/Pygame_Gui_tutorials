"""
gui_app_16.py

Animated UI Lesson:

This lesson shows to animate pygame_gui elements over time.
You will move a button smoothly across the screen and fade a label
in and out by adjusting its alpha transparency.
"""

# Import modules
import pygame
import pygame_gui

# ----------------------------------------------------------------
# Main application class
# Handles window setup, GUI manager, animations, event loop,
# drawing, and timing.
# ----------------------------------------------------------------
class App:
    def __init__(self):
        pygame.init()

        # Create main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 16 - Animated UI")

        # Create pygame_gui manager
        self.manager = pygame_gui.UIManager(
            (800, 600),
            "themes/theme_16_fade.json"
        )

        # Timing and loop control
        self.clock = pygame.time.Clock()
        self.running = True

        # ------------------------------------------------------------
        # Animated GUI elements
        # ------------------------------------------------------------

        # Button that moves horizontally
        self.moving_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 250, 150, 50),
            text="I'm Moving",
            manager=self.manager
        )

        # ------------------------------------------------------------
        # Custom fading label (manual surface so text can fade)
        # ------------------------------------------------------------
        self.label_font = pygame.font.Font(None, 36)
        self.fading_label_surface = pygame.Surface((200, 40), pygame.SRCALPHA)

        # Background stays solid so text is readable
        self.fading_label_surface.fill((0, 0, 0))

        # Animation variables
        self.button_speed = 100    # pixels per second
        self.label_alpha  = 255    # full opacity
        self.fade_direction = -1   # -1 = fade out, +1 = fade in

    # ----------------------------------------------------------------
    # Animate GUI elements
    # Called every frame with time_delta to ensure smooth animation.
    # ----------------------------------------------------------------
    def animate_elements(self, time_delta):

        # ------------------------------------------------------------
        # Move the button horizontally
        # ------------------------------------------------------------
        rect = self.moving_button.rect
        rect.x += int(self.button_speed * time_delta)

        # Reset position when it reaches the right side
        if rect.x > 600:
            rect.x = 50

        # Apply new position to the button
        self.moving_button.set_relative_position((rect.x, rect.y))

        # ------------------------------------------------------------
        # Fade the text in and out (background stays solid)
        # ------------------------------------------------------------
        self.label_alpha += int(self.fade_direction * 200 * time_delta)

        # Reverse direction at limits
        if self.label_alpha <= 40:
            self.fade_direction = 1
        elif self.label_alpha >= 255:
            self.fade_direction = -1

        # Clear background
        self.fading_label_surface.fill((0, 0, 0))

        # Render text with variable alpha
        text_surface = self.label_font.render("I'm Fading", True, (255, 255, 255))
        text_surface.set_alpha(self.label_alpha)

        # Center text on the label surface
        text_rect = text_surface.get_rect(center=self.fading_label_surface.get_rect().center)
        self.fading_label_surface.blit(text_surface, text_rect)

    # ----------------------------------------------------------------
    # Main application loop
    # Handles events, updates animations, updates GUI manager,
    # draws UI, and refreshes the screen.
    # ----------------------------------------------------------------
    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            # Process pygame events
            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

            # Animate moving and fading elements
            self.animate_elements(time_delta)

            # Update pygame_gui
            self.manager.update(time_delta)

            # Draw background and UI
            self.window.fill((20, 20, 40))
            self.manager.draw_ui(self.window)

            # Draw the fading label manually
            self.window.blit(self.fading_label_surface, (300, 100))

            pygame.display.flip()

        pygame.quit()

# ----------------------------------------------------------------
# Program entry point
# ----------------------------------------------------------------
if __name__ == "__main__":
    App().run()
