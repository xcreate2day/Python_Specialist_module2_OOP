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


if __name__ == '__main__':
    # Создадим несколько карт
    card1 = Card("10", "Hearts")
    card2 = Card("2", "Diamonds")
    card3 = Card("10", "Diamonds")

    # Выведем карты на экран в виде: 10♥ и A♦
    print(card1)
    print(card2)

    # Проверим, одинаковые ли масти у карт
    if card1.equal_suit(card2):
        print(f"У карт: {card1} и {card2} одинаковые масти")
    else:
        print(f"У карт: {card1} и {card2} разные масти")

    if card3.equal_suit(card2):
        print(f"У карт: {card3} и {card2} одинаковые масти")
    else:
        print(f"У карт: {card3} и {card2} разные масти")

    print(f'{card1 > card2 = }')
    print(f'{card1 < card2 = }')
    print(f'{card1 > card3 = }')
    print(f'{card1 < card3 = }')

    # print('\u2661', '\u2665')
    # print('\u2662', '\u2666')
    # print('\u2667', '\u2663')
    # print('\u2664', '\u2660')
