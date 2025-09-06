#Hangman Game

import random
word_list = ["apple", "banana", "cherry", "grape", "kiwi", "mango",
    "elephant", "giraffe", "kangaroo", "panda", "octopus", "dolphin",
    "astronaut", "robot", "wizard", "dragon", "pirate", "knight",
    "computer", "keyboard", "monitor", "internet", "printer", "scanner",
    "mountain", "river", "ocean", "forest", "desert", "island"
]

print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

print("")
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
print(f"The word is {word_length} letters long")

for position in range(word_length):
	placeholder += "_"
print(placeholder)
print("")
print("******************************************************")

game_over = False
correct_letter = []
lives = 6
while not game_over:
    print("")   
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else: 
            display += "_"
    print(display)


    if guess not in chosen_word:
        lives -= 1
        print("")
        print("--------------------You guessed wrong-----------------")
        print(f"---------------------{lives} lives left----------------------")
        print("")

        if lives == 0:
            game_over = True
            print("--------------------You lose-----------------------")
            print("")
            print(f"The word was {chosen_word}")
    else:
        print("")
        print("******************************************************")
        print("")
    if "_" not in display:
        game_over = True
        print("----------------------You win!!-------------------")
   
        
        