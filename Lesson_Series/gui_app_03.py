"""
gui_app_03.py

Teaches:
- UITextEntryLine
- UILabel
- Reading text input
"""

# Import modules
import pygame
import pygame_gui


class App:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 03")

        self.manager = pygame_gui.UIManager((800, 600))

        self.clock = pygame.time.Clock()
        self.running = True

        self.build_ui()


    def build_ui(self):
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(300, 150, 200, 40),
            text="Enter your name:",
            manager=self.manager
        )

        self.entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(300, 200, 200, 40),
            manager=self.manager
        )

        self.submit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(300, 260, 200, 40),
            text="Submit",
            manager=self.manager
        )


    def process_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.submit_button:
                print("You typed:", self.entry.get_text())


    def run(self):
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


