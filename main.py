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
point_error = 3
vowel = ['a', 'i', 'o', 'u', 'y', 'e']

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
    #Si la lettre est autre que l'alphabet
    if not guess.isalpha():
        print("Vous ne devez saisir que des lettres de l’alphabet.")
        if not point_error < 0:
            point_error -= 1

    # si la lettre n'est pas dans 'chosen_word', on affiche la lettre et on laisse savoir que ce n'est pas dans le mot
    elif not guess in (display and chosen_word):
        #Si la lettre est un consonne
        if guess not in vowel:
            if not lives < 0:
                lives -= 1
                lost = 1
        else:
            if not lives < 1:
                lives -= 2
                lost = 2
        print(f"Vous avez devine {guess}, elle n'est pas dans le mot. Vous perdez {lost} tentative")
    else:
        # verifier la lettre devine
        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter

    if lives == 0:
        end_game = True
    elif point_error == 0 and (not lives == 0):
        lives -= 1
        print(f"Il vous reste {lives}.")

    #Joindre tous les elements de la liste et les transformer en string
    print(f"{' '.join(display)}")
    
    #Verifier si l'utilisateur a obtenu toutes les lettres
    if '_' not in display:
        end_game = True
        print("Vous avez gagné.")

    #on importe le 'stages' de let_get_art et 
    print(stages[lives])