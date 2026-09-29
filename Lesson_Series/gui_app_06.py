"""
gui_app_06.py

Teaches:
- UIConfirmationDialog
"""

# Import modules
import pygame
import pygame_gui


class App:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 06")

        self.manager = pygame_gui.UIManager((800, 600))

        self.clock = pygame.time.Clock()
        self.running = True

        self.build_ui()

    def build_ui(self):
        self.open_dialog_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(300, 250, 200, 50),
            text="Open Dialog",
            manager=self.manager
        )

    def process_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.open_dialog_button:
                pygame_gui.windows.UIConfirmationDialog(
                    rect=pygame.Rect(200, 150, 400, 200),
                    manager=self.manager,
                    window_title="Confirm",
                    action_long_desc="Do you want to continue?",
                    action_short_name="Yes",
                    blocking=True
                )

        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            print("Dialog confirmed!")

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
