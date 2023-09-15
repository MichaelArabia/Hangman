import random
import re
from typing import List


class Hangman:
    """A simple Hangman class containing different functions to make the game work"""
    def __init__(self) -> None:
        """initializes the game with default settings"""
        self.possible_words: List[str] = [
            "becode",
            "learning",
            "mathematics",
            "sessions",
        ]
        # Randomly selects a word from possible_words
        self.word_to_find: List[str] = list(random.choice(self.possible_words).lower())
        self.lives: int = 5
        # Initialize the word with underscores
        self.correctly_guessed_letters: List[str] = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    @staticmethod
    def is_valid_input(input_str: str, pattern: str) -> bool:
        """
        Static method validates the input against the provided pattern

            Parameters:
                input_str (str): The input string to validate
                pattern (str): The regex pattern agains which to validate the input

            Returns:
                bool: True if input_str matches the pattern, False otherwise
        """
        return bool(re.match(pattern, input_str))

    def play(self) -> None:
        """Handles a single turn of the game"""

        if self.turn_count == 0:
            print("Word to find :", " ".join(self.correctly_guessed_letters))

        letter: str = input("Enter a letter : ").lower()

        # Validates the user's input
        while not Hangman.is_valid_input(letter, "^[a-zA-Z]$"):
            letter = input("Enter a single letter only: ").lower()

        self.turn_count += 1

        # Check if the letter exist in the word
        if letter in self.word_to_find:
            for index, char in enumerate(self.word_to_find):
                if char == letter:
                    self.correctly_guessed_letters[index] = letter
        else:
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(letter)

    def start_game(self) -> None:
        """Starts and manages the entire game loop"""
        while self.lives > 0 and "_" in self.correctly_guessed_letters:
            self.play()
            self.display_game_status()

        # Game over conditions
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

        # Ask user if they want to restart
        if self.ask_restart():
            print("\nRestarting the game...\n")
            self.__init__()
            self.start_game()

    def display_game_status(self) -> None:
        """Display the current game status"""
        print("Correctly guessed letters:", " ".join(self.correctly_guessed_letters))
        print("Wrongly guessed letters:", " ".join(self.wrongly_guessed_letters))
        print("Lives:", self.lives)
        print("Turn count:", self.turn_count)
        print("Error count:", self.error_count)

    def ask_restart(self) -> bool:
        """
        Ask the user if they want to restart the game

            Returns:
                bool: Return the user's input choice
        """
        choice = input("Do you want to restart the game ? (y/n): ").lower()
        while not Hangman.is_valid_input(choice, "^[yn]$"):
            choice = input("Enter only y for yes or n for no ").lower()
        return choice == "y"

    def game_over(self) -> None:
        """Displays the game over message and reveals the word to guess"""
        print(f"Game over... The word to guess was : {''.join(self.word_to_find)}")

    def well_played(self) -> None:
        """Congratulates the user for guessing the word"""
        print(
            f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors"
        )
