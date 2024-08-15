import sys
import os
from unittest.mock import patch
import pytest


def setup_path():
    # Ensure the src directory is given a higher priority
    current_dir = os.path.abspath(os.path.dirname(__file__))
    src_dir = os.path.abspath(os.path.join(current_dir, "..", "src"))
    sys.path.append(src_dir)


setup_path()


@patch("random.randint")
def test_dice_roll(mock_randint):
    from CLI.player import Player  # Import after updating sys.path

    """
    Test that the dice_roll method of the Player class only uses the numbers 3 and 4 to achieve a total roll of 7.
    Mocks random.randint to return the sequence [3, 4] repeatedly and asserts the total roll is 7.
    """
    print("Running test_dice_roll...")  # Debug statement

    # Define the sequence of values to mock
    mock_randint.side_effect = [3, 4, 3, 4]  # Repeat the sequence if needed

    instance = Player(name_of_player="TestPlayer", player_id=1)

    roll_results = []
    total_roll = 0

    while total_roll != 7:
        total_roll = instance.dice_roll()
        roll_results.append(total_roll)
        print(f"Generated roll: {total_roll}")

    assert total_roll == 7


if __name__ == "__main__":
    pytest.main()
