import random
from let_get_art import logo, stages

# Mettre a jour la liste word_list par les mots dans fichier mots.txt. 
# supprimer word_list = ['putain', 'flacide', 'fils']
path = r"F:\python\projet-bootcamp1\mots.txt"
with open(path, "r") as f:
    word_list = f.read().splitlines()

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_game = False
lives = 6

#on importe le logo dans let_get_art et on l'affiche au demarrage du jeu
print(logo)


#tester le code
print(f'le mot est {chosen_word}')

#creer des espaces blancs
display = []
for _ in range(word_length):
    display += '_'


while not end_game:
    guess = input("Devine une lettre : ").lower()
    
    #Si l'utilisateur a entré une lettre qu'il a deja deviné, affiche la lettre et laissons le savoir 
    if guess in display:
        print(f"vous avez deja devine {guess}")

    #verifier la lettre devine
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    #Verifier si l'utilisateur a tort    
    if not guess in chosen_word:
        #si la lettre n'est pas dans 'chosen_word', on affiche la lettre et on laisse savoir que ce n'est pas dans le mot
        print(f"Vous avez devine {guess}, elle n'est pas dans le mot. Vous perdez une vie")
        lives -= 1
        if lives == 0:
            end_game = True
            print("Game over!")

    #Joindre tous les elements de la liste et les transformer en string
    print(f"{' '.join(display)}")
    
    #Verifier si l'utilisateur a obtenu toutes les lettres
    if '_' not in display:
        end_game = True
        print("Vous avez gagné.")

    #on importe le 'stages' de let_get_art et 
    print(stages[lives])