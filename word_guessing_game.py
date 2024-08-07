import random

def word_guess_game():
    lives = 3

    words = ['mango', 'apple', 'peach', 'grape', 'melon', 'guava']
    print(f"Fruits words to guess: {words}")
    secret_word = random.choice(words)

    clue = list('-----')
    heart_symbol = u'\u2764'

    guessed_word_correctly = False

    def update_clue(guessed_letter, secret_word, clue):
        index = 0
        while index < len(secret_word):
            if guessed_letter == secret_word[index]:
                clue[index] = guessed_letter
            index = index + 1

    while lives > 0:
        print(clue)
        print('Lives left: ' + heart_symbol * lives)
        guess = input('Guess a letter or the whole word: ')

        if guess == secret_word or clue == list(secret_word):
            guessed_word_correctly = True
            break

        if guess in secret_word:
            update_clue(guess, secret_word, clue)
        else:
            print('Incorrect. You lose a life')
            lives = lives - 1

    if guessed_word_correctly:
        print('You won! The secret word was ' + secret_word)
    else:
        print('You lost! The secret word was ' + secret_word)


if __name__ == "__main__":
    word_guess_game()