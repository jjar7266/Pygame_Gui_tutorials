"""
gui_app_02.py

Demonstrates:
- UIWindow
- Buttons inside/outside window
- ObjectID (class_id + object_id)
- Theme loading
- Visual debug mode
"""

# Import modules
import pygame
import pygame_gui
from pygame_gui.core import ObjectID


class App:
    def __init__(self):
        pygame.init()

        self.WINDOW_SIZE = (800, 600)
        self.window = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("GUI APP 02")

        self.manager = pygame_gui.UIManager(
            self.WINDOW_SIZE,
            theme_path="theme_01.json"
        )

        self.manager.set_visual_debug_mode(True)

        self.clock = pygame.time.Clock()
        self.running = True

        self.build_ui()

    def build_ui(self):
        """ Create UI elements. """

        # Window container
        self.ui_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(100, 50, 300, 200),
            window_display_title="Demo Window",
            manager=self.manager,
            object_id=ObjectID(object_id="#demo_window")
        )

        # Button inside window
        self.hello_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(30, 30, 120, 40),
            text="Say Hello",
            manager=self.manager,
            container=self.ui_window,
            object_id=ObjectID(
                class_id='@friendly_buttons',
                object_id="#hello_button"
            )
        )

        # Button outside window
        self.debug_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(350, 300, 160, 40),
            text="Toggle Debug",
            manager=self.manager,
            object_id=ObjectID(
                class_id='@friendly_buttons',
                object_id='#debug_button'
            )
        )

    def process_events(self, event):
        """ Handle button presses. """
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == self.hello_button:
                print("Hello from inside the window!")

            if event.ui_element == self.debug_button:
                self.manager.set_visual_debug_mode(
                    not self.manager.visual_debug_active
                )

    def run(self):
        """ Main loop. """
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                self.process_events(event)

            self.manager.update(time_delta)

            self.window.fill((0, 0, 0))
            self.manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()


