# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле


class Car:
    def __init__(self,  color, count_passenger_seats,is_baby_seat, is_busy):
        self.color=color
        self.count_passenger_seats=count_passenger_seats
        self.is_baby_seat=is_baby_seat
        self.is_busy=is_busy

    def __str__(self):
        print(f'Автомобиль: (цвет= {self.color}, количество пассажирских мест={self.count_passenger_seats},\
наличие десткого кресла={self.is_baby_seat},  в работе={self.is_busy})')

car=Car('Белый', '4', '2', '1')
car.__str__()