import random
from typing import Self

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}

class Card:
    # TODO: сюда копируем реализацию класса карты из предыдущего задания
    #  реализуем новые методы
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __repr__(self):
        return self.__str__()

    def equal_suit(self, other: Self):
        return self.suit == other.suit

    def __gt__(self, other: Self):
        if self.value == other.value:
            return SUITS.index(self.suit) > SUITS.index(other.suit)
        return VALUES.index(self.value) > VALUES.index(other.value)

    def __lt__(self, other: Self):
        if self.value == other.value:
            return SUITS.index(self.suit) < SUITS.index(other.suit)
        return VALUES.index(self.value) < VALUES.index(other.value)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return f'deck[{len(self.cards)}] {", ".join([str(card) for card in self.cards])}'


    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_taken = [card for card in self.cards[:x]]
        self.cards = self.cards[x:]
        return cards_taken

    def shuffle(self) -> None:
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.__gt__(card2):
    print(f"{card1} больше {card2}")
if card1.__lt__(card2):
    print(f"{card1} меньше {card2}")
