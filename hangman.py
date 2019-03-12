TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'


# DO NOT MODIFY THE initialize function
def initialize(word_list):
    """
    Takes a list of words as a parameter.
    Starting with the word in the word_list,
    starts a new game using the word.
    If the user wants to play again, starts the next
    game with the next word.
    Runs until user doesn't want to play or
    until it runs out of new words.
    """
    i = 0
    while i < len(word_list) and start_new_game(word_list[i], TRIES):
        i += 1


def obfuscate(word, letters_guessed):
    """
    Takes the current word being guessed and
    a string containing letters that user has
    tried to guess during current playthrough.
    Returns a string, that only shows letters
    that the user has guessed correctly. Return
    the guessed letter in uppercase. The letters,
    that user still has to guess are replaced with
    underscores.
    Example:
        input: 'claire','abcd'
        ouput: 'C_A___'
    Example:
        input: 'Amanda','etai'
        output: 'A_A__A'
    Example:
        input: 'Obi-Wan KENOBI','oteai'
        output: 'O_I-_A_ _E_O_I'
    """
    return ''.join(l if not l.isalpha() or l in letters_guessed.upper() else '_' for l in word.upper())



def start_new_game(word, max_tries):
    """
    # Arguments
    Takes a word (string) that the user has to guess,
    and max_tries (int) - the number of tries user has
    before he loses the game.
    # Description
    Before prompting the user always show the letters he still hasn't tried to guess.
    This function should prompt user for a letter, and
    check, whether the letter guessed is in the word.
    If user guessed correctly, reveal the letter to him.
    If user guessed wrong, decrease the number of tries and show the amount of tries remaining.
    Keep asking user for more letters, until he wins or loses.
    When the game ends, ask user to choose, whether they want
    to play the game again.
    If the user types 'n', return False.
    If the user types 'y', return True.
    User will only input 'n','N','y' or 'Y', so no need to handle other cases
    # Return
    Returns a boolean, stating whether user
    wants to have another game.
    Example:
        input: 'Obi-Wan Kenobi',
        execution: user wins, wants to play again,
                    types 'y' when prompted
        output: True
    Example:
        input: 'GANDALF',
        execution: user wins, doesn't want to play again,
                    types 'n' when prompted
        output: False
    """
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    tries_left = max_tries
    letters_guessed = []

    print(obfuscate(word, ''.join(letters_guessed)))

    won = False

    while tries_left:
        print(LETTERS_LEFT)
        print(''.join(l for l in ALPHABET if l not in letters_guessed))
        print(INPUT_PROMPT)
        value = input()

        if value and len(value) == 1 and value.isalpha():
            value = value.upper()

            if value not in letters_guessed and value not in word.upper():
                tries_left -= 1
                print(f'{REMAINING_TRIES}{tries_left}')

            letters_guessed += value

            result = obfuscate(word, ''.join(letters_guessed))
            print(result)

            if result.upper() == word.upper():
                won = True
                break
        else:
            print(INVALID_INPUT)

    if won:
        print(GAME_WON_PHRASE)
    else:
        print(GAME_LOST_PHRASE)

    print(OFFER_NEXT_GAME)
    value = input()

    return value.upper() == 'Y'


# initialize(['Obi-Wan Kenobi', 'Alladin'])