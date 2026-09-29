"""
gui_app_11.py

This program teaches:
 - How to make a HUD (Heads-UP Display)
 - How to show GUI elements on top of a game screen
 - How to update HUD values (like score or health)
 - How to keep HUD elements visible at all times

HUDS are used in:
 - Games (health, score, ammo)
 - Tools (status indicators)
 - Apps (always-visible info)

We will make:
 - A score label
 - A health bar
 - A button that increases score
 - A button that decreases health
"""

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
        pygame.display.set_caption("GUI App 11 - HUD Overlay")

        # The GUI manager controls all GUI elements
        self.manager = pygame_gui.UIManager((800, 600))

        # Helps us keep track of time
        self.clock = pygame.time.Clock()

        # Tells the program when to stop
        self.running = True

        # HUD values
        self.score = 0
        self.health = 100

        # Build all GUI elements
        self.build_ui()


    def build_ui(self):
        """
        Build the HUD elements.
        HUD elements sit at the top of the screen.
        """

        # ---------------------------------------------------------
        # SCORE LABEL
        # ---------------------------------------------------------
        self.score_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(20, 20, 150, 40),
            text="Score: 0",
            manager=self.manager
        )

        # ----------------------------------------------------------
        # HEALTH BAR
        # ----------------------------------------------------------
        self.health_bar = pygame_gui.elements.UIProgressBar(
            relative_rect=pygame.Rect(20, 70, 200, 30),
            manager=self.manager
        )
        self.health_bar.max_progress = 100
        self.health_bar.set_current_progress(self.health)


        # ------------------------------------------------------------
        # BUTTONS TO CHANGE HUD VALUES
        # ------------------------------------------------------------

        # Increase score
        self.add_score_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 120, 150, 40),
            text="Add Score",
            manager=self.manager
        )

        # Decrease health
        self.damage_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 170, 150, 40),
            text="Take Damage",
            manager=self.manager
        )


    def process_events(self, event):
        """
        Handle button presses.
        """

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Increase score
            if event.ui_element == self.add_score_button:
                self.score += 10
                self.score_label.set_text(f"Score: {self.score}")
                print(f"Score is now {self.score}")

            # Decrease score
            if event.ui_element == self.damage_button:
                self.health -= 10
                if self.health < 0:
                    self.health = 0

                self.health_bar.set_current_progress(self.health)

                print(f"Health is now {self.health}")


    def draw_game_background(self):
        """
        Draw a simple fake game background.
        In a real game, this would be your game world.
        """

        # Fill with dark blue to simulate a game screen
        self.window.fill((10, 20, 60))

        # Draw a simple circle to pretend it's a game object
        pygame.draw.circle(self.window, (200, 50, 50), (400, 300), 50)


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

            # Draw the fake game world first
            self.draw_game_background()

            # Draw the HUD on top of the game world
            self.manager.draw_ui(self.window)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    App().run()







