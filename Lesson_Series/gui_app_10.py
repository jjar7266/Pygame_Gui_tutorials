"""
gui_app_10.py
This program teaches:
- How to make MULTIPLE GUI windows
- How to show and hide windows
- How to switch between windows using buttons

This is very useful for:
- Tools with multiple screens
- Settings windows
- Inventory windows
- Any app that needs more than one window
"""

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
        pygame.display.set_caption("GUI App 10 - Multi-Window GUI")

        # The GUI manager controls all GUI elements
        self.manager = pygame_gui.UIManager((800, 600))

        # Helps us keep track of time
        self.clock = pygame.time.Clock()

        # Tells the program when to stop
        self.running = True

        # Build all GUI elements
        self.build_ui()

    def build_ui(self):
        """
        Build the main window and the secondary window.
        """

        # ---------------------------------------------------------
        # MAIN WINDOW
        # ---------------------------------------------------------
        self.main_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(100, 50, 300, 200),
            window_display_title="Main Window",
            manager=self.manager
        )

        # Button inside main window that opens the second window
        self.open_second_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 80, 200, 40),
            text="Open Second Window",
            manager=self.manager,
            container=self.main_window
        )

        # ---------------------------------------------------------
        # SECOND WINDOW
        # ---------------------------------------------------------
        self.second_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(450, 50, 300, 200),
            window_display_title="Second Window",
            manager=self.manager
        )

        # Button inside second window that hides it
        self.close_second_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 80, 200, 40),
            text="Hide This Window",
            manager=self.manager,
            container=self.second_window
        )

        # Start with the second window hidden
        self.second_window.hide()

    def process_events(self, event):
        """
        Handle button presses.
        """

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # If the user clicked the "Open Second Window" button
            if event.ui_element == self.open_second_button:
                self.second_window.show()
                print("Second window opened!")

            # If the user clicked the "Hide This Window" button
            if event.ui_element == self.close_second_button:
                self.second_window.hide()
                print("Second window hidden!")

    def run(self):
        """
        Main loop.
        """

        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():

                # Quit first
                if event.type == pygame.QUIT:
                    self.running = False

                # GUI events
                self.manager.process_events(event)
                self.process_events(event)

            # Update GUI
            self.manager.update(time_delta)

            # Draw everything
            self.window.fill((0, 0, 0))
            self.manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
