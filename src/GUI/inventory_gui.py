import pygame
from src.GUI.inventory import Inventory

class InventoryGUI:
    """Graphical User Interface to display the player's inventory."""

    def __init__(self, screen: pygame.Surface, inventory: Inventory) -> None:
        self.screen = screen
        self.inventory = inventory 
        self.font = pygame.font.Font(None, 36)
        self.running = False

        # Button dimmentions
        self.button_width = 100
        self.button_height = 50

        # Initialize button actions 
        self.button_actions = {}

    def draw_buttons(self, x: int, y: int, item: str) -> None:
        """Draw Use and Discard buttons for a specific item."""
        use_button = pygame.Rect(x, y, self.button_width, self.button_height)
        discard_button = pygame.Rect(x + self.button_width + 10, y, self.button_width, self.button_height)

        pygame.draw.rect(self.screen, (0, 255, 0), use_button) # Green
        pygame.draw.rect(self.screen, (150, 75, 0), discard_button) # Brown

        use_text = self.font.render("Use", True, (0, 0, 0)) # Black
        discard_text = self.font.render("Discard", True, (0, 0, 0)) 

        self.screen.blit(use_text, (x + 10, y + 10))
        self.screen.blit(discard_text, (x + self.button_width + 20, y + 10))

        return use_button, discard_button
     
    def draw(self):
        """Draw the inventory overlay."""
        self.screen.fill((0, 0, 0)) # Solid Black background

        # Reset button actions
        self.button_actions = {}

        # Draw the inventory items
        y_offset = 50 # Start below the title
        for item, quantity in self.inventory.get_items().items():
            # Display item and quantity
            text = self.font.render(f"{item}: {quantity}", True, (255, 255, 255)) # White
            self.screen.blit(text, (50, y_offset))

            # Draw buttons
            use_button, discard_button = self.draw_buttons(300, y_offset, item)

            # Store buttonr references for event handling
            self.button_actions[item] = (use_button, discard_button)
            y_offset += 60 # Move down for the next item

        # Draw hint 
        hint_text = self.font.render("Press 'I' to close inventory", True, (200, 200, 200)) # Light gray text
        self.screen.blit(hint_text, (50, y_offset + 20)) 

    def handle_mouse_click(self, mouse_pos):
        """handle mouse clicks on buttons."""
        for item, (use_button, discard_button) in self.button_actions.items():
            if use_button.collidepoint(mouse_pos):
                print(self.inventory.use_item(item)) # Example: Use the item
            elif discard_button.collidepoint(mouse_pos):
                print(self.inventory.remove_item(item, 1)) # Example: Discard the item