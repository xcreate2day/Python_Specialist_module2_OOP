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
    # TODO: сюда копируем реализацию класса колоды из предыдущего задания
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def __str__(self):
        return f'{self.__class__.__name__}[{len(self.cards)}] {", ".join([str(card) for card in self.cards])}'
            
    def __repr__(self):
        return self.__str__()

    # def __getitem__(self, index):


    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_taken = self.cards[:x]
        self.cards = self.cards[x:]
        return cards_taken

    def shuffle(self) -> None:
        random.shuffle(self.cards)


if __name__ == '__main__':

    deck = Deck()
    # Задачи - реализовать нативную работу с объектами:
    # 1. Вывод колоды в терминал:
    print(deck)  # вместо print(deck.show())

    card1, card2 = deck.draw(2)
    # 2. Вывод карты в терминал:
    print(card1, card2)  # вместо print(card1.to_str())

    # 3. Сравнение карт:
    if card1 > card2:
        print(f"{card1} больше {card2}")
    if card1 < card2:
        print(f"{card1} less than {card2}")

    deck.shuffle()
    print(deck)

    card3, card4 = deck.draw(2)
    # 2. Вывод карты в терминал:
    print(card3, card4)  # вместо print(card1.to_str())

    # 3. Сравнение карт:
    #print(VALUES.index(card3[0]), VALUES.index(card4[0]))
    if card3 > card4:
        print(f"{card3} больше {card4}")
    if card3 < card4:
        print(f"{card3} less than {card4}")

    # Это на следующее занятие.
    # 4. Итерация по колоде:
    # for card in deck:
    #     print(card)

    # 5. Просмотр карты в колоде по ее индексу:
    # __getitem__(self, index):
    # print(deck[6])


# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html


