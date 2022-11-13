import random
word_list = ['putain', 'flacide', 'fils']
chosen_word = random.choice(word_list)
print(f'le mot est {chosen_word}')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)
"""on utilise un while loop pour laisser l'utilisateur deviner encore. la boucle ne s'arrete que lorsque toutes les lettres ont ete devines dans 'chosen_word' et display n'a plus de '_'. Donc l'utilisateur a gagne."""
end_game = False
while not end_game:
    guess = input("Devine une lettre : ").lower()
    
    #verifier la lettre devine
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
        
    print(display)

    #verifie si il n'y a plus de '_' dans display. si c'est le cas, toutes les lettres ont ete devines 
    if '_' not in display:
        end_game = True
        print("Vous avez gagné.")