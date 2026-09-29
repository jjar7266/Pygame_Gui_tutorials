"""
gui_app_18.py - File Browser UI (Mock)

File Browser Lesson:

This lesson shows how to build a simple mock file browser using
pygame_gui's UISelectionList. You will react to selection changes
and simulate "Open" and "Delete" actions for the selected file.
"""

# Import modules
import pygame
import pygame_gui

# -----------------------------------------------------------------
# Main application class
# Handles window setup, GUI manager, file list UI, event logic,
# drawing, and timing.
# -----------------------------------------------------------------
class App:
    def __init__(self):
        pygame.init()

        # Create main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 18 - File Browser UI")

        # Create pygame_gui manager
        self.manager = pygame_gui.UIManager((800, 600))

        # Timing and loop control
        self.clock = pygame.time.Clock()
        self.running = True

        # Build all UI elements
        self.build_ui()

    # ---------------------------------------------------------------
    # Build the file browser UI
    # Creates a selection list and two buttons (Open / Delete).
    # ---------------------------------------------------------------
    def build_ui(self):

        # File list (mock data)
        self.file_list = pygame_gui.elements.UISelectionList(
            relative_rect=pygame.Rect(100, 80, 300, 400),
            item_list=[
                "save_01.dat",
                "save_02.dat",
                "config.json",
                "log.txt",
                "profile_joe.cfg",
                "profile_guest.cfg"
            ],
            manager=self.manager
        )

        # Open button
        self.open_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(450, 150, 200, 50),
            text="Open File",
            manager=self.manager
        )

        # Delete button
        self.delete_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(450, 220, 200, 50),
            text="Delete File",
            manager=self.manager
        )

        # Currently selected file
        self.selected_file = None

    # ---------------------------------------------------------------
    # Event processing for file selection and button actions
    # ---------------------------------------------------------------
    def process_events(self, event):

        # -----------------------------------------------------------
        # Handle new selection from the file list
        # -----------------------------------------------------------
        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            if event.ui_element == self.file_list:
                self.selected_file = event.text
                print(f"Selected: {self.selected_file}")

        # -----------------------------------------------------------
        # Handle button presses (Open / Delete)
        # -----------------------------------------------------------
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Open file action
            if event.ui_element == self.open_button and self.selected_file:
                print(f"Opening file: {self.selected_file}")

            # Delete file action
            if event.ui_element == self.delete_button and self.selected_file:
                print(f"Deleting file: {self.selected_file}")

    # ------------------------------------------------------------------
    # Main application loop
    # Handles events, updates GUI manager, draws UI, and refreshes screen.
    # ------------------------------------------------------------------
    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            # Process pygame events
            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                # Custom file browser event handling
                self.process_events(event)

            # Update pygame_gui
            self.manager.update(time_delta)

            # Draw background and UI
            self.window.fill((25, 25, 35))
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()


# -------------------------------------------------------------------
# Program entry point
# -------------------------------------------------------------------
if __name__ == "__main__":
    App().run()

    


