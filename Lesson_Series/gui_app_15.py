"""
gui_app_15.py

Custom Widget (Manual Pygame Drawing)

Custom Widget: A simple colored box that acts like a button.

This program teaches:
 - How to make a "custom widget" using a normal pygame.Rect
 - How to draw it yourself
 - How to detect clicks inside it
 - How to mix pygame_gui with your own drawing
 - How to integrate custom widgets into a class-based GUI app
"""

# Import modules
import pygame
import pygame_gui


# -----------------------------------------------------------
# Main application class
# Handles window setup, GUI manager, custom widget logic,
# event processing, drawing, and the main loop.
# -----------------------------------------------------------
class App:
    def __init__(self):
        pygame.init()

        # Create main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 15 - Custom Widget")

        # Create pygame_gui manager
        self.manager = pygame_gui.UIManager((800, 600))

        # Timing and loop control
        self.clock = pygame.time.Clock()
        self.running = True

        # -----------------------------------------------------------
        # Custom widget setup
        # This is NOT a pygame_gui element. It's a manual pygame.Rect.
        # We will draw it ourselves and handle its events manually.
        # -----------------------------------------------------------
        self.custom_box = pygame.Rect(300, 200, 200, 100)

        # Colors for different interaction states
        self.default_color = (100, 180, 250)
        self.hover_color   = (130, 200, 255)
        self.clicked_color = (250, 120, 120)
        self.custom_box_color = self.default_color

        # GUI label explaining the custom widget
        self.info_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(250, 100, 300, 40),
            text="Click the blue box!",
            manager=self.manager
        )

    # -------------------------------------------------------------
    # Event processing for the custom widget
    # Handles hover detection and click detection.
    # pygame_gui does NOT handle events for custom widgets.
    # -------------------------------------------------------------
    def process_events(self, event):

        # Hover effect (mouse moves over the box)
        if event.type == pygame.MOUSEMOTION:
            if self.custom_box.collidepoint(event.pos):
                self.custom_box_color = self.hover_color
            else:
                self.custom_box_color = self.default_color

        # Click detection (left mouse button)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.custom_box.collidepoint(event.pos):
                    print("Custom box clicked!")
                    self.custom_box_color = self.clicked_color

    # -------------------------------------------------------------
    # Draw the custom widget manually
    # pygame_gui cannot draw custom widgets, so we draw it ourselves.
    # This must happen BEFORE manager.draw_ui().
    # -------------------------------------------------------------
    def draw_custom_box(self):
        pygame.draw.rect(self.window, self.custom_box_color, self.custom_box)

    # ---------------------------------------------------------------
    # Main application loop
    # Handles event processing, GUI updates, drawing, and screen refresh.
    # ---------------------------------------------------------------
    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            # Process pygame events
            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                # Custom widget event handling
                self.process_events(event)

            # Update pygame_gui
            self.manager.update(time_delta)

            # Drawing order:
            # 1. Clear background
            # 2. Draw custom widget
            # 3. Draw pygame_gui elements
            self.window.fill((30, 30, 30))
            self.draw_custom_box()
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()

# -------------------------------------------------------
# Program entry point
# -------------------------------------------------------
if __name__ == "__main__":
    App().run()


