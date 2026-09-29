"""
gui_app_13.py

This program teaches:
 - How to make an INVENTORY GRID
 - How to place GUI elements in rows and columns
 - How to detect which inventory slot was clicked
 - How to store item names inside slots

Inventory grids are used in:
 - RPG games
 - Crafting systems
 - Storage chests
 - Equipment screens

We will make:
 - A 4x4 inventory grid (16 slots)
 - Each slot is a button
 - clicking a slot prints which item is inside
"""

# Import modules
import pygame
import pygame_gui


class InventorySlot:
    """
    A tiny helper class that stores:
    - The button for the slot
    - The item name inside the slot
    """

    def __init__(self, button, item_name):
        self.button = button
        self.item_name = item_name


class App:
    """
    This class represents our whole GUI program.
    """

    def __init__(self):
        pygame.init()

        # Make the main window
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GUI App 13 - Inventory UI")

        # The GUI manager controls all GUI elements
        self.manager = pygame_gui.UIManager((800, 600))

        # Helps us keep track of time
        self.clock = pygame.time.Clock()

        # Tells the program when to stop
        self.running = True

        # A list to store all inventory slots
        self.inventory_slots = []

        # Build all GUI elements
        self.build_ui()


    def build_ui(self):
        """
        Build a 4x4 inventory grid.
        Each slot is a button.
        """

        # Grid settings
        rows = 4
        cols = 4
        slot_size = 100
        start_x = 150
        start_y = 100

        # Example items to place in the inventory
        items = [
            "Sword", "Shield", "Potion", "Bow",
            "Helmet", "Armor", "Boots", "Ring",
            "Gem", "Key", "Map", "Torch",
            "Herbs", "Scroll", "Coin", "Empty"
        ]

        # Build the grid
        index = 0
        for row in range(rows):
            for col in range(cols):

                # Position of each slot
                x = start_x + col * slot_size
                y = start_y + row * slot_size

                # Create the button for the slot
                button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(x, y, 90, 90),
                    text=items[index],
                    manager=self.manager
                )

                # Store the slot
                slot = InventorySlot(button, items[index])
                self.inventory_slots.append(slot)

                index += 1


    def process_events(self, event):
        """
        Handle inventory slot clicks.
        """

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Check every inventory slot
            for slot in self.inventory_slots:
                if event.ui_element == slot.button:
                    print(f"You clicked on: {slot.item_name}")


    def draw_game_background(self):
        """
        Draw a simple fake game background.
        """

        self.window.fill((40, 40, 40))

        # Title text
        font = pygame.font.SysFont(None, 48)
        text = font.render("Inventory", True, (200, 200, 200))
        self.window.blit(text, (320, 20))


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
            self.draw_game_background()

            # Draw GUI on top
            self.manager.draw_ui(self.window)

            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    App().run()



