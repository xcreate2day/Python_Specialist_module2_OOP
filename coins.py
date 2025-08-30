import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.choice(['heads', 'tails'])  # random.randint(0, 1)

    # def __repr__(self):
    #     return f'{self.side}'


n = int(input('Введите количество монет: '))

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

coins = [Coin() for _ in range(n)]
for coin in coins:
    coin.flip()

# Выведите соотношение выпавших орлов и решек в процентах
heads_cnt = 0
for coin in coins:
    if coin.side == 'heads':
        heads_cnt += 1
print(f'{heads_cnt / (n - heads_cnt):.2%}')





