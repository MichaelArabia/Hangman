import random
import re
from typing import List

class Hangman:
    def __init__(self) -> None:
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: List[str] = list(random.choice(self.possible_words).lower())
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    @staticmethod
    def is_valid_input(input_str: str, pattern: str) -> bool:
        return bool(re.match(pattern, input_str))

    def play(self) -> None:

        letter: str = input("Enter a letter : ").lower()
 
        while not Hangman.is_valid_input(letter, "^[a-zA-Z]$"):
            letter = input("Enter a single letter only: ").lower()

        self.turn_count += 1

        if letter in self.word_to_find:
            for index, char in enumerate(self.word_to_find):
                if char == letter:
                    self.correctly_guessed_letters[index] = letter
        else:
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(letter)

    def start_game(self) -> None:
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            self.play()
            self.display_game_status()

        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

        if self.ask_restart():
            print("\nRestarting the game...\n")
            self.__init__()
            self.start_game()


    def display_game_status(self) -> None:
        print("Correctly guessed letters:", ' '.join(self.correctly_guessed_letters))
        print("Wrongly guessed letters:", ' '.join(self.wrongly_guessed_letters))
        print("Lives:", self.lives)
        print("Turn count:", self.turn_count)
        print("Error count:", self.error_count)

    def ask_restart(self) -> bool:
        choice = input("Do you want to restart the game ? (y/n): ").lower()
        while not Hangman.is_valid_input(choice, "^[yn]$"):
            choice = input("Enter only y for yes or n for no").lower() 
        return choice == "y"

    def game_over(self) -> None:
        print(f"Game over... The word to guess was : {''.join(self.word_to_find)}")

    def well_played(self) -> None:
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors")