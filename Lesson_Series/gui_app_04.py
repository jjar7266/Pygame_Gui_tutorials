"""
gui_app_04.py

Teaches:
- UIHorizontalSlider
- UIDropDownMenu
"""

# Import modules
import pygame
import pygame_gui


class App:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 04")

        self.manager = pygame_gui.UIManager((800, 600))

        self.clock = pygame.time.Clock()
        self.running = True

        self.build_ui()

    def build_ui(self):
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(200, 150, 400, 40),
            start_value=50,
            value_range=(0, 100),
            manager=self.manager
        )

        self.dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=["Easy", "Medium", "Hard"],
            starting_option="Medium",
            relative_rect=pygame.Rect(200, 250, 200, 40),
            manager=self.manager
        )

    def process_events(self, event):
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            print("Slider:", event.value)

        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            print("Difficulty:", event.text)

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
