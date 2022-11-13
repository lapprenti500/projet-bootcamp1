import random
word_list = ['putain', 'flacide', 'fils']
chosen_word = random.choice(word_list)

guess = input("Devine une lettre : ").lower()

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")