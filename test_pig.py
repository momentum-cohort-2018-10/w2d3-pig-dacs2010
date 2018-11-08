from pig import Die, Player

# testing the die
def test_die_roll():
    roll = Die(1) 
    assert roll.number == 1
    roll = Die(2)
    assert roll.number == 2

