options = ['Rock', 'Paper', 'Scissors']


def get_player_choices():
    import random
    player_1 = None
    while not player_1 in options:
        player_1 = input('Rock, Paper, or Scissors?')
    player_2 = random.choice(options)

    return player_1, player_2

def get_winner(player_1, player_2):
    if not player_1 in options: return False
    if not player_2 in options: return False
    # to make life a little easier
    rock = options[0]
    paper = options[1]
    scissors = options[2]
    tie = "It's a tie!"
    p1_wins = "player 1 wins!"
    p2_wins = "player 2 wins!"

    if (player_1 == player_2): return tie
    if (player_1 == rock and player_2 == scissors): return p1_wins
    if (player_1 == paper and player_2 == rock): return p1_wins
    if (player_1 == scissors and player_2 == paper): return p1_wins
    return p2_wins



def test_get_player_choices():
    p1, p2 = get_player_choices()
    assert p1 in options, 'Test Failed: Invalid choice for player 1'
    assert p2 in options, 'Test Failed: Invalid choice for player 2'
    print("All Tests passed for get_player_choices()")

def test_get_winner():
    tie_output = "It's a tie!"
    p1_output = "player 1 wins!"
    p2_output = "player 2 wins!"
    # Test Invalid Input
    print("Test Invalid input ...")
    assert get_winner(None, 'Rock') == False, "Test Failed: Invalid input for player 1 should return False."
    assert get_winner('Rock', None) == False, "Test Failed: Invalid input for player 2 should return False."
    print("Tests passed!")
    # Test Tie
    print("Test Tie ...")
    assert get_winner('Rock','Rock') == tie_output, "Test Failed: Same input should return 'It's a Tie!'"
    assert get_winner('Paper','Paper') == tie_output, "Test Failed: Same input should return 'It's a Tie!'"
    assert get_winner('Scissors','Scissors') == tie_output, "Test Failed: Same input should return 'It's a Tie!'"
    print("Tests passed!")
    # Test Player 1 wins
    print("Test player 1 wins ...")
    assert get_winner('Rock', 'Scissors') == p1_output, "Test Failed: Player 1 wins should return 'player 1 wins!'"
    assert get_winner('Paper', 'Rock') == p1_output, "Test Failed: Player 1 wins should return 'player 1 wins!'"
    assert get_winner('Scissors', 'Paper') == p1_output, "Test Failed: Player 1 wins should return 'player 1 wins!'"
    print("Tests passed!")
    # Test Player 2 wins
    print("Test player 2 wins ...")
    assert get_winner('Scissors', 'Rock') == p2_output, "Test Failed: Player 2 wins should return 'player 2 wins!'"
    assert get_winner('Rock', 'Paper') == p2_output, "Test Failed: Player 2 wins should return 'player 2 wins!'"
    assert get_winner('Paper', 'Scissors') == p2_output, "Test Failed: Player 2 wins should return 'player 2 wins!'"
    print("Tests passed!")
    print("All tests passed for get_winner()")

test_get_winner()