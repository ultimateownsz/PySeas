import pygame
from src.GUI.inventory import Inventory

class InventoryGUI:
    """Graphical User Interface to display the player's inventory."""

    def __init__(self, screen: pygame.Surface, inventory: Inventory) -> None:
        self.screen = screen
        self.inventory = inventory 
        self.font = pygame.font.Font(None, 36)
        self.running = False

        # Load sprite sheet and extract the icons 
        self.sprite_sheet = pygame.image.load("images/tilesets/Treasure+.png").convert_alpha()
        self.icons = {
            "Gold Coin": self.extract_icon(0, 0),
            "Silver Coin": self.extract_icon(16, 0),
            "Coin Stack (1)": self.extract_icon(32, 0),}

        # Button dimmentions
        self.button_width = 100
        self.button_height = 50

        # Initialize button actions 
        self.button_actions = {}

        # Action messages
        self.message = ""
        self.message_end_time = 0 # Time to display the message

    def extract_icon(self, x, y, size = 16):
        """Extract a single icon from the sprite sheet."""
        return self.sprite_sheet.subsurface((x, y, size, size))

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
            # Draw icon 
            if item in self.icons:
                self.screen.blit(self.icons[item], (50, y_offset))

            # Draw quantity next to the icon
            quantity_text = self.font.render(f"x{quantity}", True, (255, 255, 255))
            self.screen.blit(quantity_text, (100, y_offset + 5))

            # Draw item name (move text to the right)
            text = self.font.render(item, True, (255, 255, 255))
            self.screen.blit(text, (150, y_offset))

            # Draw buttons
            use_button, discard_button = self.draw_buttons(400, y_offset, item)

            # Store buttonr references for event handling
            self.button_actions[item] = (use_button, discard_button)
            y_offset += 60 # Move down for the next item

        # Draw hint 
        hint_text = self.font.render("Press 'I' to close inventory", True, (200, 200, 200)) # Light gray text
        self.screen.blit(hint_text, (50, y_offset + 20)) 

        # Display action message at the bottom
        if self.message and pygame.time.get_ticks() < self.message_end_time:
            message_text = self.font.render(self.message, True, (255, 255, 0)) # Yellow
            self.screen.blit(message_text, (50, y_offset + 50))

    def handle_mouse_click(self, mouse_pos):
        """Handle mouse clicks on buttons."""
        for item, (use_button, discard_button) in self.button_actions.items():
            if use_button.collidepoint(mouse_pos):
                self.message = self.inventory.use_item(item)
                self.message_end_time = pygame.time.get_ticks() + 3000 # 3 seconds
            elif discard_button.collidepoint(mouse_pos):
                self.message = self.inventory.remove_item(item, 1)
                self.message_end_time = pygame.time.get_ticks() + 4000 # 4 seconds