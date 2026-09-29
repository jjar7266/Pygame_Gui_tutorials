"""
gui_app_05.py

Teaches:
- UIScrollingContainer
- Adding elements inside scrollable area
"""

# Import modules
import pygame
import pygame_gui


class App:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI APP 05")

        self.manager = pygame_gui.UIManager((800, 600))

        self.clock = pygame.time.Clock()
        self.running = True

        self.build_ui()

    def build_ui(self):
        self.scroll_panel = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect(100, 100, 300, 300),
            manager=self.manager
        )

        # Add multiple label inside the scroll panel
        for i in range(20):
            pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(10, i * 40, 350, 30),
                text=f"Item {i + 1}",
                manager=self.manager,
                container=self.scroll_panel
            )

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

            self.manager.update(time_delta)

            self.window.fill((0, 0, 0))
            self.manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()


