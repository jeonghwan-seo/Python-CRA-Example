import pytest


class Player:
    ...


def test_game_player_effect():
    level = 10
    hp = 180
    mp = 200
    name = "hwan"

    # level up effect
    hp += 10
    mp -= 20
    level += 1

    assert hp == 190
    assert mp == 180
    assert level == 11
