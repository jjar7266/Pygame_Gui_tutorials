"""
gui_app_07.py

Teaches:
- How to make TABS (like in a web browser) using normal buttons
- How to switch between different screens
- How to organize GUI content into panels

We will make:
Tab 1: A simple label
Tab 2: A button
Tab 3: A text entry box
"""

import pygame
import pygame_gui


class App:
    def __init__(self):
        pygame.init()

        # Main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 07 - Tabs (Stable Version)")

        # GUI manager
        self.manager = pygame_gui.UIManager((800, 600))

        # Clock
        self.clock = pygame.time.Clock()
        self.running = True

        # Build UI
        self.build_ui()

    def build_ui(self):
        """Build the tab bar and tab panels."""

        # --- TAB BUTTONS (acting as tabs) ---
        self.tab1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 50, 100, 40),
            text="Tab 1",
            manager=self.manager
        )

        self.tab2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(150, 50, 100, 40),
            text="Tab 2",
            manager=self.manager
        )

        self.tab3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(250, 50, 100, 40),
            text="Tab 3",
            manager=self.manager
        )

        # --- PANELS FOR EACH TAB ---
        self.tab1_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(50, 100, 700, 450),
            manager=self.manager
        )

        self.tab2_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(50, 100, 700, 450),
            manager=self.manager
        )

        self.tab3_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(50, 100, 700, 450),
            manager=self.manager
        )

        # --- CONTENT INSIDE EACH PANEL ---
        self.tab1_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(250, 200, 200, 40),
            text="This is Tab 1",
            manager=self.manager,
            container=self.tab1_panel
        )

        self.tab2_button_inside = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(250, 200, 200, 40),
            text="Click Me!",
            manager=self.manager,
            container=self.tab2_panel
        )

        self.tab3_entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(250, 200, 200, 40),
            manager=self.manager,
            container=self.tab3_panel
        )

        # --- Show Tab 1 first ---
        self.show_tab(1)

    def show_tab(self, tab_index):
        """Show one tab panel and hide the others."""
        self.tab1_panel.hide()
        self.tab2_panel.hide()
        self.tab3_panel.hide()

        if tab_index == 1:
            self.tab1_panel.show()
        elif tab_index == 2:
            self.tab2_panel.show()
        elif tab_index == 3:
            self.tab3_panel.show()

    def process_events(self, event):
        """Handle button presses and tab switching."""
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            # Tab bar buttons
            if event.ui_element == self.tab1_button:
                self.show_tab(1)
            elif event.ui_element == self.tab2_button:
                self.show_tab(2)
            elif event.ui_element == self.tab3_button:
                self.show_tab(3)

            # Button inside Tab 2
            if event.ui_element == self.tab2_button_inside:
                print("You clicked the Tab 2 button!")

    def run(self):
        """Main loop."""
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.manager.process_events(event)
                self.process_events(event)

            self.manager.update(time_delta)
            self.window.fill((0, 0, 0))
            self.manager.draw_ui(self.window)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
