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


hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in VALUES:
    hearts_cards.append((value, SUITS[3]))

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in VALUES:
    diamonds_cards.append((value, SUITS[2]))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(', '.join([f'{value}{SUITS_UNI[suit]}' for value, suit in hearts_cards]))

print(', '.join([f'{value}{SUITS_UNI[suit]}' for value, suit in diamonds_cards]))
