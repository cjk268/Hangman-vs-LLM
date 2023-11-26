import random

class Hangman: 
    def __init__(self) -> None:
        self.lives = 7
        self.guessed_letters = []
        self.guess = ""
        self.word = self.choose_word()
        self.word_progress = self.starting_blanks()
        self.game_won = False

    def choose_word(self, txt_file_path="wordlist.txt"):
        try:
            with open(txt_file_path, mode="r") as file:
                words = file.readlines()
                return random.choice(words).replace("\n", "")
        except FileNotFoundError:
            print("The file does not exist.")
        except Exception as e:
            print(f"An error has occured: {e}")

    def starting_blanks(self): 
        start_blanks = ""
        start_blanks = ["_ " for _ in self.word]
        return start_blanks

    def update_word_progress(self):
        for index, letter in enumerate(self.word):
            if letter == self.guess:
                self.word_progress[index] = letter

    def play_turn(self): 
        # displaying word progress
        print("".join(self.word_progress))

        self.guess = input("Guess a letter: ").lower()
        
        # Checks valid input
        if len(self.guess) != 1 or not self.guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
        
        else:
            if self.guess in self.guessed_letters:
                print(f"You have guessed {self.guess} already, try again.\n")
            
            elif self.guess not in self.word:
                self.lives -= 1
                print(f"Incorrect! You have {self.lives} remaining.\n")
                self.guessed_letters.append(self.guess)

            elif self.guess in self.word:
                self.update_word_progress()
                self.guessed_letters.append(self.guess)
                print("Yep, it's in there, nice!\n")

            else:
                print("An error has occured, this is embarrassing")
            
            # converts self.word_progress from list to string and checks for win
            if "".join(self.word_progress) == self.word:
                self.game_won = True
                print(f"Nice! You got it, the word was: {self.word}")
                
    def start_game(self):
        print(hangman.word)
        while self.lives > 0 and not self.game_won:
            self.play_turn()
        
        if not self.game_won:
            print(f"Sorry, you have ran out of attempts, the word was: {self.word}")



if __name__ == "__main__":
    hangman = Hangman()
    hangman.start_game()
    