import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
lives = 6
end_of_game = False


print(hangman_art.logo)
display = []

# Create blanks
for letter in chosen_word:
    display += "_"

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    # Check if letter is already guessed
    if guess in display:
        print(f"You already have typed the {guess} letter")
        
    # Check guessed letter
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess


    if guess not in chosen_word:
        lives -= 1
        print(f"The {guess} letter you have typed is not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose")
    
     #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    
    # check if exists blanck spaces
    if not "_" in display:
        end_of_game = True
        print("You win")

    print(hangman_art.stages[lives])
    