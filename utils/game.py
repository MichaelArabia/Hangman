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

    def play(self) -> None:

        letter: str = input("Enter a letter : ").lower()
 
        while not re.match("^[a-zA-Z]$", letter):
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
            print("Correctly guessed letters : ", ' '.join(self.correctly_guessed_letters))
            print("Wrongly guessed letters : ", ' '.join(self.wrongly_guessed_letters))
            print("Lives : ", self.lives)
            print("Turn count : ", self.turn_count)
            print("Error count : ", self.error_count)

        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

    def game_over(self) -> None:
        print("game over")

    def well_played(self) -> None:
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors")