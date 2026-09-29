"""
basic_gui_02.py

A beginner-friendly pygame-gui example demonstrating:

- UIWindow (container)
- Buttons inside and outside the window
- ObjectID usage (class_id + object_id)
- Theme loading
- Visual debug mode

This script pairs with theme_01.json
"""

# Import modules
import pygame
import pygame_gui
from pygame_gui.core import ObjectID


def main():
    # Initialize Pygame
    pygame.init()

    WINDOW_SIZE = (800, 600)
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Beginner GUI 02")

    # Load theme_01.json
    manager = pygame_gui.UIManager(WINDOW_SIZE, theme_path="themes/theme_01.json")

    # Show selector chains on screen (very helpful for learning)
    manager.set_visual_debug_mode(True)

    clock = pygame.time.Clock()
    running = True

    # Colors
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)

    FPS = 60

    # UIWindows (acts like a container)
    ui_window = pygame_gui.elements.UIWindow(
        rect=pygame.Rect(100, 50, 300, 200),
        window_display_title="Demo Window",
        manager=manager,
        object_id=ObjectID(object_id="#demo_window")
    )

    # Button INSIDE the window
    hello_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(30, 30, 120, 40),
        text="Say Hello",
        manager=manager,
        container=ui_window,
        object_id=ObjectID(
            class_id='@friendly_buttons',
            object_id='#hello_button'
        )
    )

    # Button OUTSIDE the window
    debug_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(350, 300, 160, 40),
        text="Toggle Debug",
        manager=manager,
        object_id=ObjectID(
            class_id='@friendly_buttons',
            object_id='#debug_button'
        )
    )

    # Main Loop
    while running:
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            manager.process_events(event)

            if event.type == pygame.QUIT:
                running = False

            # BUtton Press Handling
            if event.type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == hello_button:
                    print("Hello from inside the window!")

                if event.ui_element == debug_button:
                    manager.set_visual_debug_mode(
                        not manager.visual_debug_active
                    )

        manager.update(time_delta)

        window.fill(BLACK)
        manager.draw_ui(window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()


