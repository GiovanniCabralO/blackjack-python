from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(user_score, comp_score, user, comp):
    if user_score > 21:
        return "You went over. You lose 😵‍💫"
    if comp_score > 21:
        return "Computer went over. You win! 🥳"
    if user_score == comp_score:
        return "It's a draw."
    if user_score == 21 and len(user) == 2:
        return "Blackjack! You win!!"
    if comp_score == 21 and len(comp) == 2:
        return "Computer has a Blackjack. You lose."
    return "You win! 😁" if user_score > comp_score else "You lose 😭"

def calculate_score(user, comp):
    while sum(user) > 21 and 11 in user:
        user[user.index(11)] = 1
    while sum(comp) > 21 and 11 in comp:
        comp[comp.index(11)] = 1
    return sum(user), sum(comp)


def game():

    print("\n" * 25)
    print(logo)

    user = []
    comp = []

    user.extend(random.choices(cards, k=2))
    comp.extend(random.choices(cards, k=2))
    score_user, score_comp = calculate_score(user, comp)

    while score_comp < 17:
        comp.append(random.choice(cards))
        score_user, score_comp = calculate_score(user, comp)

    print(f"Your cards: {user}, current score: {score_user}")
    print(f"Computer's first card: {comp[0]}")

    while score_user < 21:
        another = input("Type 'y' to get another card, type 'n' to pass: ")

        if another == 'y':
            user.append(random.choice(cards))
            score_user, score_comp = calculate_score(user, comp)
            print(f"Your cards: {user}, current score: {score_user}")
            print(f"Computer's first card: {comp[0]}")
        else:
            break

    print(f"\nYour final hand: {user}, final score: {score_user}")
    print(f"Computer's final hand: {comp}, final score: {score_comp}")
    print(compare(score_user, score_comp, user, comp))

def main():
    while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        game()

main()

print("\nThanks for playing! 🃏\n")
