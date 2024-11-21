import pygame
from src.GUI.inventory import Inventory

class InventoryGUI:
    """Graphical User Interface to display the player's inventory."""

    def __init__(self, screen: pygame.Surface, inventory: Inventory) -> None:
        self.screen = screen
        self.inventory = inventory 
        self.font = pygame.font.Font(None, 36)
        self.running = False

    def draw(self):
        """Draw the inventory overlay."""
        self.screen.fill((0, 0, 0))

        # Draw the inventory items
        y_offset = 50 # Start below the title
        for item, quantity in self.inventory.get_items().items():
            text = self.font.render(f"{item}: {quantity}", True, (255, 255, 255)) # White text
            self.screen.blit(text, (50, y_offset))
            y_offset += 40 # Move down for the next item

        # Draw hint 
        hint_text = self.font.render("Press 'I' to close inventory", True, (200, 200, 200)) # Light gray text
        self.screen.blit(hint_text, (50, y_offset + 20)) 