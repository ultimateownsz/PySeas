import sys
import os
from unittest.mock import patch
import pytest

# Ensure the src directory is giving the module a higher priority
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
# print("sys.path:", sys.path)  # Uncomment for debugging the sys.path

from py_version.player import Player

@patch('random.randint')
def test_dice_roll(mock_randint):
    '''
    Test that the dice_roll method of the Player class only uses the numbers 3 and 4 to achieve a total roll of 7.
    Mocks random.randint to return the sequence [3, 4] repeatedly and asserts the total roll is 7.
    '''
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
