"""
gui_app_17.py

Drag-and-Drop Lesson:

This lesson shows how to make a pygame_gui panel draggable.
You will detect mouse down on the panel, drag it while the mouse
moves, and stop dragging when the mouse button is released.
"""

# Import modules
import pygame
import pygame_gui

# -------------------------------------------------------------------
# Main application class
# Handles window setup, GUI manager, drag logic, event loop,
# drawing, and timing.
# -------------------------------------------------------------------
class App:
    def __init__(self):
        pygame.init()

        # Create main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 17 - Drag and Drop UI")

        # Create pygame_gui manager
        self.manager = pygame_gui.UIManager((800, 600))

        # Timing and loop control
        self.clock = pygame.time.Clock()
        self.running = True

        # ------------------------------------------------------------
        # Draggable panel
        # UIPanel is a pygame_gui container element.
        # We will manually move it using set_relative_position().
        # ------------------------------------------------------------
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(25, 150, 300, 200),
            starting_height=1,
            manager=self.manager
        )

        # Drag state variables
        self.dragging = False
        self.drag_offset = (0, 0)

        # Label inside the panel
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(50, 80, 200, 40),
            text="Drag me!",
            manager=self.manager,
            container=self.panel
        )

    # -----------------------------------------------------------------
    # Event processing for drag-and-drop
    # Handles drag start, drag movement, and drag end.
    # -----------------------------------------------------------------
    def process_events(self, event):

        # -------------------------------------------------------------
        # Start dragging when left mouse button is pressed
        # -------------------------------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            # Use absolute rect so the panel does NOT jump
            if self.panel.get_abs_rect().collidepoint(event.pos):

                self.dragging = True

                # Calculate offset between mouse and panel position
                mouse_x, mouse_y = event.pos
                panel_x, panel_y = self.panel.get_abs_rect().topleft
                self.drag_offset = (mouse_x - panel_x, mouse_y - panel_y)

        # -------------------------------------------------------------------
        # Stop dragging when left mouse button is released
        # -------------------------------------------------------------------
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False

        # -------------------------------------------------------------------
        # Move the panel while dragging
        # -------------------------------------------------------------------
        if event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x, mouse_y = event.pos

            new_x = mouse_x - self.drag_offset[0]
            new_y = mouse_y - self.drag_offset[1]

            # ---------------------------------------------------------------
            # Keep panel inside window boundaries
            # ---------------------------------------------------------------
            new_x = max(0, min(new_x, 800 - self.panel.rect.width))
            new_y = max(0, min(new_y, 600 - self.panel.rect.height))

            # Update panel position
            self.panel.set_relative_position((new_x, new_y))

    # ----------------------------------------------------------------
    # Main application loop
    # Handles events, updates GUI manager, draws UI, and refreshes screen.
    # ----------------------------------------------------------------
    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            # Process pygame events
            for event in pygame.event.get():
                self.manager.process_events(event)

                if event.type == pygame.QUIT:
                    self.running = False

                # Custom drag-and-drop event handling
                self.process_events(event)

            # Update pygame_gui
            self.manager.update(time_delta)

            # Draw background and UI
            self.window.fill((50, 30, 30))
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()


# -------------------------------------------------------------------
# Program entry point
# -------------------------------------------------------------------
if __name__ == "__main__":
    App().run()





