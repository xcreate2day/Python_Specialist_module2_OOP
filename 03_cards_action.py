# TODO: сюда копируем реализацию класса карты из предыдущего задания
from typing import Self

# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

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

cards = [(value, suit) for suit in SUITS for value in VALUES]
# print(cards)
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
# for suit in SUITS:
#     for value in VALUES:
#         cards.append((value, suit))

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
print(f"cards[{len(cards)}] " + ', '.join([f'{value}{SUITS_UNI[suit]}' for value, suit in cards]))
