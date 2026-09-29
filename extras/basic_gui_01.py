"""
basic_gui_01.py

A minimal pygame-gui example for beginners.

This script teaches:
- How to initialize pygame-gui
- How to create a simple button
- How to process UI events
- How to draw the UI each frame
"""

# Import modules
import pygame
import pygame_gui

# Initialize Pygame
pygame.init()

def main():

    # COLORS
    WHITE = (255, 255, 255)
    BLACK = (  0,   0,   0)

    FPS = 60

    # Create the display window
    WINDOW_SIZE = (800, 600)
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Beginner GUI 01")

    # Create the UI Manager
    # - This object controls ALL pygame-gui elements
    manager = pygame_gui.UIManager(WINDOW_SIZE)

    clock = pygame.time.Clock()
    running = True

    # Create a simple button
    # - relative_rect defines its position and size
    hello_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(350, 250, 100, 50),
        text="Hello",
        manager=manager
    )

    # Main Loop
    while running:
        time_delta = clock.tick(FPS) / 1000.0

        # Process events
        # - pygame-gui needs EVERY pygame event
        for event in pygame.event.get():
            manager.process_events(event)

            if event.type == pygame.QUIT:
                running = False

            # Handle button presses
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print("Hello World!")

        # Update UI logic
        manager.update(time_delta)

        # Draw everything
        window.fill(BLACK)  # Background
        manager.draw_ui(window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

