"""
gui_app_12.py

This program teaches:
 - How to make a PAUSE MENU for a game
 - How to show and hide the pause menu
 - How to freeze the game while the menu is open
 - How to place GUI elements on top of the game screen

Pause menus are used in:
 - Every game ever made
 - Tools that need a temporary stop
 - Apps that need a modal overlay

We will make:
 - A fake game background
 - A pause button
 - A pause menu window
 - Resume + Quit buttons
"""

# Import modules
import pygame
import pygame_gui


class App:
    """
    This class represents our whole GUI program.
    """

    def __init__(self):
        pygame.init()

        # Make the main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 12 - Pause Menu")

        # The GUI manager controls all GUI elements
        self.manager = pygame_gui.UIManager((800, 600))

        # Helps us keep track of time
        self.clock = pygame.time.Clock()

        # Tells the program when to stop
        self.running = True

        # Whether the game is paused
        self.paused = False

        # Build all GUI elements
        self.build_ui()


    def build_ui(self):
        """
        Build the pause button and the pause menu window.
        """

        # ----------------------------------------------------------
        # PAUSE BUTTON (always visible)
        # ----------------------------------------------------------
        self.pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 20, 120, 40),
            text="Pause",
            manager=self.manager
        )

        # -----------------------------------------------------------
        # PAUSE MENU WINDOW (hidden at first)
        # -----------------------------------------------------------
        self.pause_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(250, 150, 300, 300),
            window_display_title="Paused",
            manager=self.manager
        )

        # Resume button
        self.resume_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 80, 200, 50),
            text="Resume Game",
            manager=self.manager,
            container=self.pause_window
        )

        # Quit button
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 150, 200, 50),
            text="Quit Game",
            manager=self.manager,
            container=self.pause_window
        )

        # Hide the pause menu at the start
        self.pause_window.hide()


    def process_events(self, event):
        """
        Handle button presses.
        """

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Pause button clicked
            if event.ui_element == self.pause_button:
                self.paused = True
                self.pause_window.show()
                print("Game paused!")

            # Resume button clicked
            if event.ui_element == self.resume_button:
                self.paused = False
                self.pause_window.hide()
                print("Game resumed!")

            # Quit button clicked
            if event.ui_element == self.quit_button:
                print("Game quit!")
                self.running = False

        # Also allow pausing with the ESC key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Toggle pause state
                self.paused = not self.paused

                if self.paused:
                    self.pause_window.show()
                    print("Game paused!")
                else:
                    self.pause_window.hide()
                    print("Game resumed!")

    def draw_game_background(self):
        """
        Draw a simple fake game background.
        In a real game, this would be your game world.
        """

        # Fill with dark green to simulate a game screen
        self.window.fill((20, 80, 20))

        # Draw a simple moving circle to pretend it's a game object
        pygame.draw.circle(self.window, (200, 200, 50), (400, 300), 50)


    def run(self):
        """
        Main loop.
        """

        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                self.process_events(event)

            # If the game is paused, DO NOT update game logic
            if not self.paused:
                # Game logic would go here
                pass

            self.manager.update(time_delta)

            # Draw the fake game world first
            self.draw_game_background()

            # Draw the GUI on top
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
