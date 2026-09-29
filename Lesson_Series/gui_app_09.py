"""
gui_app_09.py

Teaches:
- How to make progress bar
- How to make a loading bar that fills over time
- How to update the bar using code
- How to trigger progress changes with a button

Progress bars are used in:
- Games (loading screens)
- Tools (file downloads)
- Apps (showing progress)
"""

# Import modules
import pygame
import pygame_gui


class App():
    """
    This class represents our whole GUI program.
    """

    def __init__(self):
        pygame.init()

        # Main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI APP 09 - Progress Bars")

        # GUI manager
        self.manager = pygame_gui.UIManager((800, 600))

        # Clock
        self.clock = pygame.time.Clock()
        self.running = True

        # Loading bar value
        self.loading_value = 0

        # Build UI
        self.build_ui()

    def build_ui(self):
        """
        Build the progress bar and the button that fills it.
        """

        # Manual progress bar (starts at 0%)
        self.progress_bar = pygame_gui.elements.UIProgressBar(
            relative_rect=pygame.Rect(200, 200, 400, 50),
            manager=self.manager
        )

        # Button that increases the progress bar
        self.fill_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(300, 300, 200, 50),
            text="Fill Progress",
            manager=self.manager
        )

        # Automatic loading bar
        self.loading_bar = pygame_gui.elements.UIProgressBar(
            relative_rect=pygame.Rect(200, 400, 400, 50),
            manager=self.manager
        )

    def process_events(self, event):
        """
        Handle button presses.
        """

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == self.fill_button:
                # Increase progress bar by 10%
                new_value = self.progress_bar.current_progress + 10

                # Cap at 100%
                if new_value > 100:
                    new_value = 100

                self.progress_bar.set_current_progress(new_value)
                print(f"Progress Bar: {new_value}%")

    def update_loading_bar(self, time_delta):
        """
        Slowly fill the loading bar over time.
        """

        # Increase loading value by 60 per second (nice visible speed)
        self.loading_value += 60 * time_delta

        # Cap at 100%
        if self.loading_value > 100:
            self.loading_value = 100

        # Correct setter for pygame-gui 0.6.14
        self.loading_bar.set_current_progress(self.loading_value)
        print("loading_value =", self.loading_value)

    def run(self):
        """
        Main loop.
        """

        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():

                # Quit
                if event.type == pygame.QUIT:
                    self.running = False

                # GUI events
                self.manager.process_events(event)
                self.process_events(event)

            # Update loading bar
            self.update_loading_bar(time_delta)

            # Update and draw UI
            self.manager.update(time_delta)
            self.window.fill((0, 0, 0))
            self.manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
