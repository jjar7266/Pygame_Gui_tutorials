"""
gui_app_14.py

This program teaches:
 - How to make a SETTINGS MENU
 - How to use sliders, dropdowns, and checkboxes
 - How to apply or reset settings
 - How to organize settings inside a panel

Settings menus are used in:
 - Games (volume, difficulty, graphics)
 - Tools (preference)
 - Apps (user options)

We will make:
 - A volume slider
 - A difficulty dropdown
 - A fullscreen checkbox
 - Apply + Reset buttons
"""

# Import modules
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
        pygame.display.set_caption("GUI App 14 - Settings Menu")

        # The GUI manager controls all GUI elements
        self.manager = pygame_gui.UIManager((800, 600))

        # Helps us keep track of time
        self.clock = pygame.time.Clock()

        # Tells the program when to stop
        self.running = True

        # Settings values
        self.volume = 50
        self.difficulty = "Medium"
        self.fullscreen = False

        # Build all GUI elements
        self.build_ui()


    def build_ui(self):
        """
        Build the settings panel and all controls inside it.
        """

        # -----------------------------------------------------
        # SETTINGS PANEL
        # -----------------------------------------------------
        self.settings_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(200, 80, 400, 440),
            manager=self.manager
        )

        # ------------------------------------------------------
        # VOLUME SLIDER
        # ------------------------------------------------------
        self.volume_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(50, 20, 300, 40),
            text="Volume:",
            manager=self.manager,
            container=self.settings_panel
        )

        self.volume_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(50, 60, 300, 40),
            start_value=self.volume,
            value_range=(0, 100),
            manager=self.manager,
            container=self.settings_panel
        )

        # -----------------------------------------------------------
        # DIFFICULTY DROPDOWN
        # -----------------------------------------------------------
        self.difficulty_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(50, 120, 300, 40),
            text="Difficulty:",
            manager=self.manager,
            container=self.settings_panel
        )

        self.difficulty_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=["Easy", "Medium", "Hard"],
            starting_option=self.difficulty,
            relative_rect=pygame.Rect(50, 160, 300, 40),
            manager=self.manager,
            container=self.settings_panel
        )

        # -----------------------------------------------------------
        # FULLSCREEN CHECKBOX
        # -----------------------------------------------------------
        self.fullscreen_checkbox = pygame_gui.elements.UISelectionList(
            relative_rect=pygame.Rect(50, 220, 300, 80),
            item_list=["Fullscreen"],
            manager=self.manager,
            container=self.settings_panel
        )

        # If fullscreen is true, pre-select the checkbox
        if self.fullscreen:
            self.fullscreen_checkbox.select_item("Fullscreen")

        # ------------------------------------------------------------
        # APPLY + RESET BUTTONS
        # ------------------------------------------------------------
        self.apply_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 320, 130, 50),
            text="Apply",
            manager=self.manager,
            container=self.settings_panel
        )

        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(220, 320, 130, 50),
            text="Reset",
            manager=self.manager,
            container=self.settings_panel
        )


    def process_events(self, event):
        """
        Handle slider changes, dropdown changes, checkbox changes,
        and button presses.
        """

        # ---------------------------------------------------------
        # SLIDER MOVED
        # ---------------------------------------------------------
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == self.volume_slider:
                self.volume = event.value
                print(f"Volume changed to {self.volume}")

        # ----------------------------------------------------------
        # DROPDOWN CHANGED
        # ----------------------------------------------------------
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.difficulty_dropdown:
                self.difficulty = event.text
                print(f"Difficulty changed to {self.difficulty}")

        # -----------------------------------------------------------
        # CHECKBOX CHANGED
        # -----------------------------------------------------------
        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            if event.ui_element == self.fullscreen_checkbox:
                self.fullscreen = True
                print("Fullscreen enabled")

        if event.type == pygame_gui.UI_SELECTION_LIST_DROPPED_SELECTION:
            if event.ui_element == self.fullscreen_checkbox:
                self.fullscreen = False
                print("Fullscreen disabled")

        # ----------------------------------------------------------
        # BUTTON PRESSED
        # ----------------------------------------------------------
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Apply settings
            if event.ui_element == self.apply_button:
                print("Settings Applied:")
                print(f" Volume: {self.volume}")
                print(f" Difficulty: {self.difficulty}")
                print(f" Fullscreen: {self.fullscreen}")

            # Reset settings
            if event.ui_element == self.reset_button:
                print("Settings Reset!")

                # Reset values
                self.volume = 50
                self.difficulty = "Medium"
                self.fullscreen = False

                # Reset GUI elements
                self.volume_slider.set_current_value(self.volume)

                self.difficulty_dropdown.kill()
                self.difficulty_dropdown = pygame_gui.elements.UIDropDownMenu(
                    options_list=["Easy", "Medium", "Hard"],
                    starting_option=self.difficulty,
                    relative_rect=pygame.Rect(50, 160, 300, 40),
                    manager=self.manager,
                    container=self.settings_panel
                )

                # Reset fullscreen checkbox
                self.fullscreen_checkbox.selected_items = []


    def draw_background(self):
        """
        Draw a simple background behind the settings panel.
        """

        self.window.fill((30, 30, 30))

        # Title text
        font = pygame.font.SysFont(None, 48)
        text = font.render("Settings Menu", True, (200, 200, 200))
        self.window.blit(text, (260, 20))


    def run(self):
        """
        Main loop.
        """

        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                self.process_events(event)

            self.manager.update(time_delta)

            # Draw background first
            self.draw_background()

            # Draw GUI on top
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()


