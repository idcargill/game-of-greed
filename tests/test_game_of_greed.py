import pytest
from game_of_greed import __version__
from game_of_greed.game_logic import GameLogic, Banker

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def zero_score():
    zero_score = (2,3,4,6)
    return zero_score


def test_zilch(zero_score):
    result = GameLogic.calculate_score(zero_score)
    assert result == 0
    
@pytest.mark.parametrize('input ,output', [((1),100), ((1,1),200), ((1,1,1), 1000), ((1,1,1,1), 2000), ((1,1,1,1,1),4000), ((1,1,1,1,1,1), 8000 )])   
def test_ones(input, output):
    assert GameLogic.calculate_score(input) == output

@pytest.mark.parametrize('input, output', [((2),0), ((2,2), 0), ((2,2,2), 200), ((2,2,2,2), 400), ((2,2,2,2,2), 800), ((2,2,2,2,2,2),1600)])
def test_twos(input, output):
    assert GameLogic.calculate_score(input) == output

@pytest.mark.parametrize('input, output', [ ((3), 0), ((3,3), 0), ((3,3,3), 300), ((3,3,3,3), 600), ((3,3,3,3,3), 1200), ((3,3,3,3,3,3), 2400)])
def test_threes(input, output):
    assert GameLogic.calculate_score(input) == output

@pytest.mark.parametrize('input, output', [((4), 0), ((4,4), 0), ((4,4,4), 400), ((4,4,4,4), 800), ((4,4,4,4,4), 1600), ((4,4,4,4,4,4), 3200)])
def test_fours(input, output):
    assert GameLogic.calculate_score(input) == output

@pytest.mark.parametrize('input, output', [ ((5), 50), ((5,5), 100), ((5,5,5), 500), ((5,5,5,5), 1000), ((5,5,5,5,5), 2000), ((5,5,5,5,5,5), 4000)])
def test_fives(input, output):
    assert GameLogic.calculate_score(input) == output

@pytest.mark.parametrize('input, output', [ ((6), 0), ((6,6), 0), ((6,6,6), 600), ((6,6,6,6), 1200), ((6,6,6,6,6), 2400), ((6,6,6,6,6,6), 4800)])
def test_sixes(input, output):
    assert GameLogic.calculate_score(input) == output

def test_straight():
    score = (6,4,5,3,1,2)
    result = GameLogic.calculate_score(score)
    assert result == 1500

def test_three_pairs():
    score = (6,5,6,5,3,3)
    result = GameLogic.calculate_score(score)
    assert result == 1000

def test_two_trios():
    score = (3,3,3,4,4,4)
    result = GameLogic.calculate_score(score)
    assert result == 700

# Banker
@pytest.fixture
def banker():
    return Banker()

def test_banker_shelf(banker):
    banker.shelf(500)
    assert banker.unbanked == 500

def test_banker_bank(banker):
    banker.shelf(444)
    banker.bank()
    assert banker.banked == 444

def test_clear_shelf(banker):
    banker.shelf(500)
    banker.bank()
    banker.clear_shelf()
    assert banker.unbanked == 0

def test_clear_shelf_bank(banker):
    banker.shelf(500)
    banker.bank()
    banker.clear_shelf()
    assert banker.banked == 500