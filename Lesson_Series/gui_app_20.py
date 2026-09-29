"""
gui_app_20.py - Mini App (pygame_gui 0.6.10 compatible):

This lesson combines multiple GUI patterns into one small
control center application. It demostrates:

- A custom tab system (Status / Settings)
- A status panel with console logging
- A settings panel with sliders and dropdowns
- Shared state between tabs
- Clean class-based GUI structure

This version is rewritten to work with pygame_gui 0.6.10,
which does NOT include UITabBar or UITabButton.
"""

# Import modules
import pygame
import pygame_gui

# -----------------------------------------------------------------
# Main application class
# Handles window setup, GUI manager, tab system, shared state,
# event logic, drawing, and timing.
# -----------------------------------------------------------------
class App:
    def __init__(self):
        pygame.init()

        # Create main window
        self.window = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("GUI App 20 - Mini App")

        # Create pygame_gui manager
        self.manager = pygame_gui.UIManager((900, 600))

        # Timing and loop control
        self.clock = pygame.time.Clock()
        self.running = True

        # Shared application state
        self.volume = 50
        self.difficulty = "Medium"

        # Build all UI elements
        self.build_ui()

    # -------------------------------------------------------------
    # Build the entire mini-app UI
    # Includes custom tab buttons, status panel, settings panel,
    # and all widgets inside each panel.
    # -------------------------------------------------------------
    def build_ui(self):

        # ---------------------------------------------------------
        # Custom Tab Buttons (pygame_gui 0.6.10 compatible)
        # These replace UITabBar / UITabBUtton from newer versions.
        # ---------------------------------------------------------
        self.status_tab_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 40, 120, 40),
            text="Status",
            manager=self.manager
        )

        self.settings_tab_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(180, 40, 120, 40),
            text="Settings",
            manager=self.manager
        )

        # ----------------------------------------------------------
        # Status Panel (shown by default)
        # ----------------------------------------------------------
        self.status_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(50, 90, 800, 460),
            starting_height=1,      # pygame_gui 06.10 uses starting_height
            manager=self.manager
        )

        # Status label
        self.status_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(50, 20, 300, 40),
            text="Game Status: OK",
            manager=self.manager,
            container=self.status_panel
        )

        # Console output box (HTML text)
        self.console = pygame_gui.elements.UITextBox(
            html_text="Console ready.<br>",
            relative_rect=pygame.Rect(50, 80, 700, 320),
            manager=self.manager,
            container=self.status_panel
        )

        # Button to log status messages
        self.log_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 420, 200, 40),
            text="Log Status",
            manager=self.manager,
            container=self.status_panel
        )

        # -------------------------------------------------------------
        # Settings Panel (hidden by default)
        # -------------------------------------------------------------
        self.settings_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(50, 90, 800, 460),
            starting_height=1,
            manager=self.manager
        )

        # Volume label
        self.volume_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(50, 40, 200, 40),
            text="Volume:",
            manager=self.manager,
            container=self.settings_panel
        )

        # Volume slider (0-100)
        self.volume_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(50, 80, 300, 40),
            start_value=self.volume,
            value_range=(0, 100),
            manager=self.manager,
            container=self.settings_panel
        )

        # Difficulty label
        self.difficulty_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(50, 140, 200, 40),
            text="Difficulty:",
            manager=self.manager,
            container=self.settings_panel
        )

        # Difficulty dropdown
        self.difficulty_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=["Easy", "Medium", "Hard"],
            starting_option=self.difficulty,
            relative_rect=pygame.Rect(50, 180, 300, 40),
            manager=self.manager,
            container=self.settings_panel
        )

        # Apply button
        self.apply_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 260, 150, 40),
            text="Apply",
            manager=self.manager,
            container=self.settings_panel
        )

        # ------------------------------------------------------------
        # Start on Status tab
        # ------------------------------------------------------------
        self.status_panel.show()
        self.settings_panel.hide()

        # Container for console logs
        self.log_count = 0

    # ------------------------------------------------------------
    # Append a new line of text to the console
    # UITextBox uses HTML formatting, so <br> creates a new line.
    # ------------------------------------------------------------
    def append_to_console(self, message):
        current_text = self.console.html_text
        new_text = current_text + message + "<br>"
        self.console.set_text(new_text)

    # -------------------------------------------------------------
    # Event processing for tabs, console logs, and settings changes
    # -------------------------------------------------------------
    def process_events(self, event):

        # ----------------------------------------------------------
        # Custom Tab Switching (pygame_gui 0.6.10 compatible)
        # ----------------------------------------------------------
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Switch to Status tab
            if event.ui_element == self.status_tab_button:
                self.status_panel.show()
                self.settings_panel.hide()

            # Switch to Settings tab
            if event.ui_element == self.settings_tab_button:
                self.settings_panel.show()
                self.status_panel.hide()

            # ------------------------------------------------------
            # Log Status button
            # ------------------------------------------------------
            if event.ui_element == self.log_button:
                self.log_count += 1
                self.append_to_console(f"Status log #{self.log_count}")
                print(f"Status log #{self.log_count}")

            # ------------------------------------------------------
            # Apply Settings button
            # ------------------------------------------------------
            if event.ui_element == self.apply_button:
                print("Settings Applied:")
                print(f"  Volume: {self.volume}")
                print(f"  Difficulty: {self.difficulty}")
                self.append_to_console(
                    f"Settings applied: Volume={self.volume}, Difficulty={self.difficulty}"
                )

        # ------------------------------------------------------------
        # Slider movement (Volume)
        # ------------------------------------------------------------
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == self.volume_slider:
                self.volume = event.value

        # ------------------------------------------------------------
        # Dropdown change (Difficulty)
        # ------------------------------------------------------------
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.difficulty_dropdown:
                self.difficulty = event.text

    # -----------------------------------------------------------------
    # Main application loop
    # Handles events, updates GUI manager, draws UI, and refreshes screen.
    # -----------------------------------------------------------------
    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            # Process pygame events
            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                # Custom mini-app event handling
                self.process_events(event)

            # Update pygame_gui
            self.manager.update(time_delta)

            # Draw background and UI
            self.window.fill((15, 15, 25))
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()


# ----------------------------------------------------------------
# Program entry point
# ----------------------------------------------------------------
if __name__ == "__main__":
    App().run()




