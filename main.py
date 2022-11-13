import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['putain', 'flacide', 'fils']
chosen_word = random.choice(word_list)
print(f'le mot est {chosen_word}')

display = []
word_length = len(chosen_word)

#on cree la varaible 'lives' pour savoir le nombre de vies restantes. 
# Et ce sera egale a 6
lives = 6

for _ in range(word_length):
    display += '_'


end_game = False
while not end_game:
    guess = input("Devine une lettre : ").lower()
    
    #verifier la lettre devine
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    #si 'guess' n'est pas dans 'chosen_word' on perd une vie. Et si on a plus de
    # vies, le jeu s'arrete and affiche 'vous avez perdu'
    if not guess in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("Game over!")

    print(f"{' '.join(display)}")

    #verifie si il n'y a plus de '_' dans display. si c'est le cas, toutes 
    # les lettres ont ete devines 
    if '_' not in display:
        end_game = True
        print("Vous avez gagné.")

    #On affiche le ASCII art de la liste 'stages' qui correspondent aux 
    # nombres de vies que l'utilisateur a.
    print(stages[lives])