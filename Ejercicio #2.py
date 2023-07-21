import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def get_hand_value(self):
        value = 0
        aces = 0
        for card in self.hand:
            if card.rank == "Ace":
                aces += 1
            elif card.rank in ["Jack", "Queen", "King"]:
                value += 10
            else:
                value += int(card.rank)
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value

def main():
    # Setup
    deck = Deck()
    player = Player("Player 1")
    dealer = Player("Dealer")

    # Initial deal
    for _ in range(2):
        player.draw(deck)
        dealer.draw(deck)

    # Player's turn
    while True:
        print(f"{player.name}'s hand: {[str(card) for card in player.hand]}")
        print(f"Hand value: {player.get_hand_value()}")

        if player.get_hand_value() >= 21:
            break

        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == "hit":
            player.draw(deck)
        elif choice == "stand":
            break

    # Dealer's turn
    while dealer.get_hand_value() < 17:
        dealer.draw(deck)

    # Determine the winner
    player_score = player.get_hand_value()
    dealer_score = dealer.get_hand_value()

    print(f"\n{player.name}'s hand: {[str(card) for card in player.hand]}")
    print(f"{player.name}'s hand value: {player_score}")

    print(f"\n{dealer.name}'s hand: {[str(card) for card in dealer.hand]}")
    print(f"{dealer.name}'s hand value: {dealer_score}")

    if player_score > 21:
        print("\nDealer wins! Player busts.")
    elif dealer_score > 21:
        print("\nPlayer wins! Dealer busts.")
    elif player_score == dealer_score:
        print("\nIt's a tie!")
    elif player_score > dealer_score:
        print("\nPlayer wins!")
    else:
        print("\nDealer wins!")

if __name__ == "__main__":
    main()