import random 

from phrasehunter.phrase import Phrase

class Game():
  def __init__(self):
    self.missed = 0
    self.phrases = self.create_phrases()
    self.active_phrase = self.get_random_phrase()
    self.guesses = [" "]

  def create_phrases(self):
    list_of_phrases = []
    list_of_phrases.append(Phrase("Learning new skills is an investment in yourself"))
    list_of_phrases.append(Phrase("Practice makes perfect"))
    list_of_phrases.append(Phrase("Never stop learning new skills"))
    list_of_phrases.append(Phrase("Knowledge is power"))
    list_of_phrases.append(Phrase("Keep it simple"))
    return list_of_phrases

  def get_random_phrase(self):
    return random.choice(self.phrases)
  
  def welcome(self):
    print("""
    ----------------------------------------
    Welcome to Senad's phrase guessing game!
    ----------------------------------------
    """)

  def start(self):
    self.welcome()
    while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
      print(f"\nNumber missed: {self.missed}")
      
      #Users input
      self.user_guess = self.get_guess()
      self.guesses.append(self.user_guess)
      self.active_phrase.check_guess(self.user_guess)
      self.active_phrase.display(self.guesses)

      if not self.active_phrase.check_guess(self.user_guess):
        self.missed += 1        
    if self.missed >= 5:
      self.game_over()
    else:
      print("\n\nGreat work! You made it!")

  def get_guess(self):
    return input("Your guess?:  ")

  def game_over(self):
    print(f"\n\nSorry, no more attemts left. Game over!")
