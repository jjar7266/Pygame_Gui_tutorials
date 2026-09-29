"""
gui_app_08.py

Teaches:
- How to show notification pop-up windows
- How to show small timed pop-up messages (simulated toast)
- How to trigger notifications when buttons are pressed
"""

import pygame
import pygame_gui


class App:
    def __init__(self):
        pygame.init()

        # Main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 08 - Notifications")

        # GUI manager
        self.manager = pygame_gui.UIManager((800, 600))

        # Clock
        self.clock = pygame.time.Clock()
        self.running = True

        # Toast reference
        self.toast_window = None

        # Build UI
        self.build_ui()

    def build_ui(self):
        """
        Build the buttons that trigger notifications.
        """

        # Button: normal notification window
        self.notify_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(300, 200, 200, 50),
            text="Show Notification",
            manager=self.manager
        )

        # Button: small timed pop-up (simulated toast)
        self.toast_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(300, 300, 200, 50),
            text="Show Timed Message",
            manager=self.manager
        )

    def show_notification(self):
        """
        Show a normal notification window.
        """

        pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect(200, 150, 400, 200),
            manager=self.manager,
            window_title="Notification",
            html_message="This is a normal notification window!"
        )

    def show_toast(self):
        """
        Show a small timed pop-up message.
        Works in pygame_gui 0.6.14.
        """

        # Create the toast window
        self.toast_window = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect(250, 400, 300, 120),
            manager=self.manager,
            window_title="Timed Message",
            html_message="This message will disappear soon!"
        )

        # Start a timer to close it after 2 seconds
        pygame.time.set_timer(pygame.USEREVENT + 50, 2000)

    def process_events(self, event):
        """
        Handle button presses.
        """

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == self.notify_button:
                self.show_notification()

            elif event.ui_element == self.toast_button:
                self.show_toast()

    def run(self):
        """
        Main loop.
        """

        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():

                # Handle quit
                if event.type == pygame.QUIT:
                    self.running = False

                # Handle toast timer
                elif event.type == pygame.USEREVENT + 50:
                    if self.toast_window is not None:
                        self.toast_window.kill()
                        self.toast_window = None

                # Only send GUI events to pygame_gui
                else:
                    self.manager.process_events(event)
                    self.process_events(event)

            # Update and draw UI
            self.manager.update(time_delta)
            self.window.fill((0, 0, 0))
            self.manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
