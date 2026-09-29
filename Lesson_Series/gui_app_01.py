"""
gui_app_01.py

A clean, class-based beginner pygame-gui example.

Teaches:
- UIManager
- Basic button
- Event handling
- Class-based architecture
"""

# Import modules
import pygame
import pygame_gui


class App:
    def __init__(self):
        pygame.init()

        self.WINDOW_SIZE = (800, 600)
        self.window = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("GUI App 01")

        # UI Manager controls all GUI elements
        self.manager = pygame_gui.UIManager(self.WINDOW_SIZE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.build_ui()

    def build_ui(self):
        """ Create all UI elements here. """
        self.hello_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(350, 250, 120, 50),
            text="Hello",
            manager=self.manager
        )

    def process_events(self, event):
        """ Handles pygame-gui events. """
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.hello_button:
                print("Hello World!")

    def run(self):
        """ Main loop """
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

