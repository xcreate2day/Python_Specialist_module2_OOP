"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...

# Значит должны быть значения по умолчанию
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на 100 км" (gas_per_100km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то бак заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива)
```
выведет сообщение "проехали ... километров",
в результате поездки потратится бензин и увеличится пробег.
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (количество бензина в баке и пробег)
"""


class Car:
    def __init__(self, gas: float = 0, capacity: float = 0, gas_per_100km: float = 1, mileage: float = 0) -> None:
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, liters) -> None:
        extra_gas = self.gas + liters - self.capacity
        if extra_gas < 0:
            self.gas += liters
        else:
            self.gas = self.capacity
            print(f"extra gas {extra_gas} liters")

    def ride(self, kms: float) -> None:
        need_gas = kms / 100 * self.gas_per_100km
        if need_gas <= self.gas:
            print(f'has driven {kms} kms')
            self.gas -= need_gas
            self.mileage += kms
        else:
            distance = self.gas / self.gas_per_100km * 100
            print(f'has driven only {distance} kms, then ran out of gas')
            self.gas = 0
            self.mileage += distance

    def info(self) -> None:
        print(f"current amount of gas is{self.gas}, mileage is {self.mileage}")


if __name__ == '__main__':
    car1 = Car(100, 10, 10, 0)
    car1.info()
    car1.ride(100)
    car1.info()
    car1.fill(20)
    car1.info()
