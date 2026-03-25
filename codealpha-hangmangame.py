"""
HANGMAN GAME
A simple text-based Hangman game where player guesses a word one letter at a time.
"""

import random  # Import random module to select random words

# List of 5 predefined words for the game
WORDS = ["PYTHON", "JAVASCRIPT", "PROGRAMMING", "DEVELOPER", "COMPUTER"]

def display_game_state(word_display, guessed_letters, incorrect_guesses_left):
    """
    Display the current game state including:
    - Hangman visual representation
    - Current word progress
    - Already guessed letters
    - Remaining incorrect guesses
    """
    print("\n" + "="*50)
    
    # Hangman visual based on remaining guesses
    print("HANGMAN STATUS:")
    if incorrect_guesses_left == 6:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses_left == 5:
        print("  +---+")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses_left == 4:
        print("  +---+")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses_left == 3:
        print("  +---+")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses_left == 2:
        print("  +---+")
        print("  O   |")
        print(" /|\\  |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses_left == 1:
        print("  +---+")
        print("  O   |")
        print(" /|\\  |")
        print(" /    |")
        print("      |")
        print("      |")
        print("=========")
    elif incorrect_guesses_left == 0:
        print("  +---+")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("      |")
        print("      |")
        print("=========")
    
    # Display current word progress (e.g., "P _ _ T _ _")
    print("\nCURRENT WORD:", " ".join(word_display))
    
    # Display already guessed letters
    if guessed_letters:
        print("GUESSED LETTERS:", ", ".join(sorted(guessed_letters)))
    else:
        print("GUESSED LETTERS: None")
    
    # Display remaining incorrect guesses
    print(f"INCORRECT GUESSES LEFT: {incorrect_guesses_left}")
    print("="*50)

def get_player_guess(guessed_letters):
    """
    Get a valid guess from the player:
    - Must be a single letter
    - Must be from A-Z
    - Must not have been guessed before
    """
    while True:  # Loop until valid input is received
        guess = input("\nGuess a letter: ").upper()  # Convert to uppercase for consistency
        
        # Check if input is exactly one character
        if len(guess) != 1:
            print("Please enter only one letter!")
            continue
        
        # Check if input is a letter (A-Z)
        if not guess.isalpha():
            print("Please enter a letter (A-Z)!")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter!")
            continue
        
        return guess  # Return valid guess

def main():
    """
    Main game function that controls the game flow
    """
    print("🎮 WELCOME TO HANGMAN! 🎮")
    print("Try to guess the word one letter at a time.")
    print("You have 6 incorrect guesses allowed.")
    print("Let's begin!\n")
    
    # Select a random word from the list
    secret_word = random.choice(WORDS)
    
    # Create a list to display progress (e.g., ['_', '_', '_'] for a 3-letter word)
    word_display = ['_' for _ in secret_word]
    
    # Set to store guessed letters (prevents duplicates)
    guessed_letters = set()
    
    # Track number of incorrect guesses left (starting at 6)
    incorrect_guesses_left = 6
    
    # Flag to track if game is still running
    game_over = False
    
    # Main game loop - continues until game is over
    while not game_over:
        # Display current game state
        display_game_state(word_display, guessed_letters, incorrect_guesses_left)
        
        # Get a valid guess from player
        guess = get_player_guess(guessed_letters)
        
        # Add guess to guessed letters set
        guessed_letters.add(guess)
        
        # Check if guess is in the secret word
        if guess in secret_word:
            print(f"✓ Good guess! '{guess}' is in the word!")
            
            # Update word_display to show correctly guessed letters
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_display[i] = guess
            
            # Check if player has won (no underscores left in word_display)
            if '_' not in word_display:
                display_game_state(word_display, guessed_letters, incorrect_guesses_left)
                print("\n🎉 CONGRATULATIONS! 🎉")
                print(f"You guessed the word: {secret_word}")
                print("You win!")
                game_over = True
        else:
            # Incorrect guess
            print(f"✗ Sorry, '{guess}' is NOT in the word.")
            incorrect_guesses_left -= 1
            
            # Check if player has lost (no incorrect guesses left)
            if incorrect_guesses_left == 0:
                display_game_state(word_display, guessed_letters, incorrect_guesses_left)
                print("\n💀 GAME OVER! 💀")
                print(f"The word was: {secret_word}")
                print("Better luck next time!")
                game_over = True
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            main()  # Restart the game
            break
        elif play_again in ['no', 'n']:
            print("\nThanks for playing Hangman! Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'")

# Entry point of the program
if __name__ == "__main__":
    main()