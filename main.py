import os
import random
from unicodedata import name
import art
import game_data


def compare(person1, person2, guess):
    if person1['follower_count'] > person2['follower_count'] and guess == 'a' or person2['follower_count'] > person1['follower_count'] and guess == 'b':
        return 0
    else:
        return 1


def repeat_print(person1, person2):
    print(
        f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")

    print(art.vs)

    print(
        f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")


game_over = False
info = game_data.data
score = 0
print(art.logo)
person1 = random.choice(info)

while not game_over:
    person2 = random.choice(info)
    repeat_print(person1, person2)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower
    comparison = compare(person1, person2, guess)

    if comparison == 0:
        score += 1
        os.system('clear')
        print(art.logo)
        print(f"You're right! Current score: {score}")
        person1 = person2

    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score {score}")
        game_over = True
