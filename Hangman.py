
import random 
from words import words
import string

def get_valid_word(words):
    while '_'in word or ' ':
words=ranom_choices(words)

return word

def hangman():
    word=get_valid_word(words)
    word_letters:set(word)
    alphabet=set(string.asciii_uppercase)
    used_letters=set()
    lives=6
    
    
  #getting user input \
  while len(word_letters)>0:
      print('You have used these letters' '.join(used_letters)')
      
      word_list=[letter if letter in used_letters else'-' for letter in word]
  print('Current_words: ',' '.join(word_list))
  
  
  user_letters=input('Guess a letter:').upper()
    if user_letter in alphabet -used letters:
        used_letters.add(user_letter)
    if user_letter in word_letters:
        word_letters.remove(user_letter)
else:
    lives=lives-1
    print("user letter is incorrect ")

elif user_letter in used letters:
    
    
    
     print('You have already used this letter. Please try again ')
        
 else:
     print('Invalid character. Please try again')
    
