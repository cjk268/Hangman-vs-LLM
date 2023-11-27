# Hangman-vs-LLM
This GitHub repository contains a Python implementation of the classic Hangman game, enhanced with the ability to challenge other users or any function that returns a letter, a large language model for example, in a word-guessing duel. Note that this is still a WIP. 

## Features
- **Multiple Players:** Support for both human and computer players.
- **Customizable Guessing Logic:** Computer players use customizable guess generator functions.
- **Dynamic Word Selection:** Randomly selects words from a provided wordlist file (`wordlist.txt` by default).
- **Interactive Gameplay:** Human players input guesses through the console, while computer players utilize predefined strategies.
- **Progress Tracking:** The game tracks each player's progress and remaining lives.

## Dependencies
- Python 3.x
- gpt4all (Optional)
- nous-hermes-llama2-13b.Q4_0.gguf (Optional, read Note below)

## Installation and usage
****Note:** the main.py contains a Nous Hermes AI player, you need to download the model from gpt4all.io[https://gpt4all.io/index.html] and add the local path in the example given below. The file is 7 GB and requires 16 GB ram to run locally. Alternatively, you can use any other GPT-4 compatible model with GPT4All or any function that returns a letter.
1. Clone the repository:
   git clone https://github.com/your-username/hangman-vs-llm.git
   
2. Navigate to the project directory:
   cd hangman-vs-llm

3. Edit main.py to configure the player and game settings:
Experiment with custom guess letter functions or use the provided Nous Hermes LLM function (or another GPT model, DOWNLOAD NEEDED SEE NOTE).
Specify the file path, and indicate the number of human players.

## Player and Hangman Inputs
# Player Class
- name (str): The name of the player (Required).
- is_human (bool): Set to True for a human player, False for a computer player (Default is 'True').
- guess_generator (function): A custom function for computer players to generate guesses (Default is 'None').
- initial_lives (int): The initial number of lives for the player (Default is 7 lives).

# Hangman Class
- players (list): A list of Player objects (Required)

## Example usage
1. Example usage without GPT4ALL:
```
from hangman import Hangman, Player
import random
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def random_guess_generator(word_progress):
    comp_choice = random.choice(alphabet_list)
    return comp_choice
   
hangman = Hangman(players=[
  Player(name="YOUR NAME", is_human=True, initial_lives=20),
  Player(name="OTHER HUMAN PLAYER", is_human=True, initial_lives=20),
  Player(name="Random Guess Generator", is_human=False, guess_generator=random_guess_generator, initial_lives=20)
])
hangman.start_game()
```

2. Example usage with GPT4ALL LLM
```
from hangman import Hangman, Player
from gpt4all import GPT4All
# Enter your gpt4all local path, in testing nous-hermes-llama2-13b.Q4_0 works better than mistral-7b-openorca.Q4_0, 
gpt4all_local_path = "YOUR_FILE_PATH/nous-hermes-llama2-13b.Q4_0.gguf"

nous-hermes-llama2-13b.Q4_0 
def nous_hermes_guess(word_progress):
    global gpt4all_local_path
    # Letter from nous_hermes comes out as "'a'", get_letter extracts letter
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
    model = GPT4All(gpt4all_local_path)
    with model.chat_session(system_template, prompt_template):
        response = model.generate(f'Here is the mystery word: {"".join(word_progress)}. Guess a letter in the '
                                'alphabet: ', max_tokens=5, temp=1)
        letter = get_letter(response)
        return letter
        
hangman = Hangman(players=[
Player(name="YOUR NAME", is_human=True, initial_lives=20),
Player(name="Nous", is_human=False, guess_generator=nous_hermes_guess, initial_lives=20)
])
hangman.start_game()
```

## File Structure
The project follows a simple file structure:
- hangman.py: Contains the implementation of the Player and Hangman classes.
- main.py: Illustrates how to use the classes with an example setup.
- wordlist.txt: A file containing a list of words for word selection in the game.

## License
This project is licensed under the terms of the MIT License. 
