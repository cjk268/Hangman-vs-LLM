# Example usage:
from hangman import Hangman, Player
import random
from gpt4all import GPT4All
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ENTER YOUR GPT4ALL FILE PATH HERE
nous_local_path = "YOUR_PATH/GPT4ALL_files/nous-hermes-llama2-13b.Q4_0.gguf"

if __name__ == "__main__":
    # Picks a random letter from the alphabet and can be used in Hangman([Player(name="Random Guess", is_human=False, guess_generator=random_guess_generator])
    def random_guess_generator(word_progress):
        comp_choice = random.choice(alphabet_list)
        print(comp_choice)
        return comp_choice
    
    # nous-hermes-llama2-13b.Q4_0 guesser model
    def nous_hermes_guess(word_progress):
        global nous_local_path
        # Letters from this model comes out as "'a'"
        def get_letter(result):
            for char in result:
                if char.isalpha():
                    letter = char  # Convert to lowercase for consistency, if needed
                    break
            return letter
            
        system_template = ('You are an AI Hangman player, leveraging a robust large language model to guess words by '
                        'inputting a single letter from the alphabet: "abcdefghijklmnopqrstuvwxyz" at a time until all the'
                        'letters in the mystery word are revealed')
        prompt_template = 'GAMEMASTER: {0}\nPLAYER: '

        model = GPT4All(nous_local_path)
        with model.chat_session(system_template, prompt_template):
            response = model.generate(f'Here is the mystery word: {"".join(word_progress)}. Guess a letter in the '
                                    'alphabet: ', max_tokens=5, temp=1)
            letter = get_letter(response)
            print(f"Response: {response}")
            print(f"Nous Hermes guess: {letter}")
            return letter

    # Initialising classes
    hangman = Hangman(players=[
    Player(name="YOUR NAME", is_human=True, initial_lives=20),
    Player(name="nous", is_human=False, guess_generator=nous_hermes_guess, initial_lives=20)
    ])

    # Starting game
    hangman.start_game()
