import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
used_letters = []

print(hangman_art.logo)

display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    if guess not in used_letters:  
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      if guess not in chosen_word:
          used_letters.append(guess)
          lives -= 1
          print(f"{guess} is not in the word. You lose a life.")
    else:
        print(f"You've already guessed {guess}")
      
    used_letters.append(guess)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
      end_of_game = True
      print("You Lose.")

    print(f"Lives: {lives}")
    print(hangman_art.stages[lives])