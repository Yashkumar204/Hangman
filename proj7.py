
import random
import hangman_art
import hangman_words
print(hangman_art.logo)
choosen_word= random.choice(hangman_words.word_list)
# print(choosen_word)
display = []
lives = 6


# for i in choosen_word:
#      display += "_"
# print(display)

for i in range (len(choosen_word)):
    display += "_"
print(display)

end_of_list= False
while not end_of_list:
        
    guess=input("Enter a Word ").lower()
    
    
    if guess in display:
            print("you have repeated the word")

    for position in range (len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            print("right") 
            display[position]=letter
            
        
    if guess  not in choosen_word:
        print(f"the word you gussed is incorrect, You lose life")
        lives -= 1
        print(hangman_art.stages[lives])
    if lives == 0:
        print("you lose")       
    print(display)

    if lives == 0:
        end_of_list = True
        

    if "_" not in display:
        
        end_of_list = True
        
if lives == 0:
    print("you lose")      
else:
    print(hangman_art.logo2)
    print(hangman_art.logo3)
 