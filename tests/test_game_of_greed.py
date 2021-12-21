from game_of_greed import __version__
from game_of_greed.game_logic import GameLogic, Banker

def test_version():
    assert __version__ == '0.1.0'

def test_zilch():
    r = GameLogic.calculate_score(2,3,4,6,3,2)
    assert r == 0