"""
gui_app_19.py - In - Game Console (Text Logging)

In-Game Console Lesson:

This lesson shows how to use UITextBox as a console output area.
You will append text to it, clear it, and trigger log messages
using pygame_gui buttons.
"""

# Import modules
import pygame
import pygame_gui

# -------------------------------------------------------------
# Main application class
# Handles window setup, GUI manager, console UI, event logic,
# drawing, and timing.
# --------------------------------------------------------------
class App:
    def __init__(self):
        pygame.init()

        # Create main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 19 - In - Game Console")

        # Create pygame_gui manager
        self.manager = pygame_gui.UIManager((800, 600))

        # Timing and loop control
        self.clock = pygame.time.Clock()
        self.running = True

        # Build all UI elements
        self.build_ui()

    # ---------------------------------------------------------------
    # Build the console UI
    # Creates a UITextBox for output and two buttons (Log / Clear).
    # ---------------------------------------------------------------
    def build_ui(self):

        # Console output box
        self.console = pygame_gui.elements.UITextBox(
            html_text="Console started.<br>",
            relative_rect=pygame.Rect(50, 50, 500, 300),
            manager=self.manager
        )

        # Button to append a new log message
        self.log_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 380, 200, 50),
            text="Log Message",
            manager=self.manager
        )

        # Button to clear the console
        self.clear_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(270, 380, 200, 50),
            text="Clear Console",
            manager=self.manager
        )

        # Counter for log entries
        self.log_count = 0

    # ------------------------------------------------------------------
    # Append a new line of text to the console
    # UITextBox uses HTML formatting, so <br> creates a new line.
    # ------------------------------------------------------------------
    def append_to_console(self, message):
        current_text = self.console.html_text
        new_text = current_text + message + "<br>"
        self.console.set_text(new_text)

    # -------------------------------------------------------------------
    # Event processing for console actions
    # Handles Log Message and Clear Console button presses.
    # -------------------------------------------------------------------
    def process_events(self, event):

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Log a new message
            if event.ui_element == self.log_button:
                self.log_count += 1
                self.append_to_console(f"Log entry #{self.log_count}")
                print(f"Logged message #{self.log_count}")

            # Clear the console
            if event.ui_element == self.clear_button:
                self.console.set_text("")
                self.log_count = 0
                print("Console cleared")

    # --------------------------------------------------------------------
    # Main application loop
    # Handles events, updates GUI manager, draws UI, and refreshes screen.
    # --------------------------------------------------------------------
    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            # Process pygame events
            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                # Custom console event handling
                self.process_events(event)

            # Update pygame_gui
            self.manager.update(time_delta)

            # Draw background and UI
            self.window.fill((10, 10, 20))
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()


# -----------------------------------------------------------------
# Program entry point
# -----------------------------------------------------------------
if __name__ == "__main__":
    App().run()

    
