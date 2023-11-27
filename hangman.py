import random

class Player:
    def __init__(self, name, is_human=True, guess_generator=None, initial_lives=7):
        self.name = name
        self.is_human = is_human
        self.guess_generator = guess_generator
        self.lives = initial_lives
        self.guessed_letters = []

    def make_guess(self, word_progress):
        if self.is_human:
            guess = input(f"{self.name}, guess a letter: ").lower()
            while not guess.isalpha() or len(guess) != 1 or guess in self.guessed_letters:
                print("Invalid input. Please enter a single letter that you haven't guessed before.")
                guess = input(f"{self.name}, guess a letter: ").lower()
        else:
            guess = self.guess_generator(word_progress)
        self.guessed_letters.append(guess)
        return guess

class Hangman:
    def __init__(self, players) -> None:
        self.players = players
        self.current_player_index = 0
        self.word = self.choose_word()
        self.game_word_progress = {player: ["_"] * len(self.word) for player in players}
        self.game_won = False

    def choose_word(self, txt_file_path="wordlist.txt"):
        try:
            with open(txt_file_path, mode="r") as file:
                words = file.readlines()
                return random.choice(words).replace("\n", "")
        except FileNotFoundError:
            print("The file does not exist.")
        except Exception as e:
            print(f"An error has occurred: {e}")

    def update_word_progress(self, player, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.game_word_progress[player][i] = guess

    def play_turn(self):
        current_player = self.players[self.current_player_index]

        print(f"{current_player.name}'s turn:")
        print(f"Lives: {current_player.lives}")
        print(" ".join(self.game_word_progress[current_player]))

        guess = current_player.make_guess(self.game_word_progress[current_player])
        print(guess)
        if guess not in self.word:
            current_player.lives -= 1
            print(f"Incorrect! {current_player.lives} lives remaining.\n")
        else:
            print("Yep, it's in there, nice!\n")
            self.update_word_progress(current_player, guess)

        if "".join(self.game_word_progress[current_player]) == self.word:
            self.game_won = True
            print(f"Nice! {current_player.name} got it, the word was: {self.word}")

        # Switch to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        print('---------------------------------------')

    def start_game(self):
        while all(player.lives > 0 for player in self.players) and not self.game_won:
            self.play_turn()

        if not self.game_won:
            print(f"Sorry, all players have run out of attempts, the word was: {self.word}")
