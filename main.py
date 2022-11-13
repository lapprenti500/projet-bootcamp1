import random
word_list = ['putain', 'flacide', 'fils']
chosen_word = random.choice(word_list)
print(f'le mot est {chosen_word}')
""" creer une liste vide display. Pour chaque lettre dans la liste chosen_word, ajouter un "_" dasn display. Si chosen_word est 'apple', display devrait etre ['_', '_', '_', '_', '_'] representant chaque lettre a deviner
"""
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)

guess = input("Devine une lettre : ").lower()

""" on boucle sur chaque position dans chosen_word; Si chaqque lettre a cette position correspond a 'guess' donc met cette lettre dans isplay sur cette position. Si l'utilisateur devine 'p' et le mot choisi etait 'apple', donc display devrait etre ['_', 'p', 'p', '_', '_'] """

for position in range(word_length):
    letter = chosen_word[position]
    if guess == letter:
        display[position] = letter

""" Affiche display et vous devez voir la lettre devinee correctement dans sa position et les autres remplaces par '_'"""
print(display)
