import random
from hangman_lives import stages
from word_list import word_list
from hangman_lives import logo
from replit import clear

print(logo)

 
# easy_mode = input("Turn on easy mode? (y or n) ").lower # future feature
# if lives <= 2 and easy_mode == 'y':
  # print(f"Hint: {chosen_word[random.randint(0, word_length)]}")

chosen_word = random.choice(word_list) # picking a random word.

#Testing
# print(chosen_word)

display = []
word_length = len(chosen_word)
end_of_game = False
lives = 6

for letter in chosen_word: #Creating Blanks.
  display.append('_')
print(display)

while not end_of_game: 
  guess = input("Guess a letter: ").lower()
  clear() #Clearing after every input. 
  print(logo)
  if guess in display: #Testing for already picked up letter.
    print(f"You've already guessed the letter {guess}")
    lives = lives + 1 - 1 # being nice!!!
    print(stages[lives])
  
  for position in range(word_length): # Replacing guessed letter with a blank!
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      
  if guess not in chosen_word: #Penalty
    lives -= 1
    
    print(stages[lives])
    print(f"The letter: {guess} is not in the word!")
    print(f"You have {lives} remaining lives!")
  
    if lives == 0:  # The condition for losing.
      end_of_game = True
      print("You lose!")
      print('----------')
      print(chosen_word)

  
  
  print(display)  
  
  if '_' not in display: #The condition for winning.
    end_of_game = True
    print("You Win!")
  


