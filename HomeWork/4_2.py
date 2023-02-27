# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None



class Car:
    def __init__(self,  color, count_passenger_seats,is_baby_seat, is_busy):
        self.color=color
        self.count_passenger_seats=count_passenger_seats
        self.is_baby_seat=is_baby_seat
        self.is_busy=is_busy

    def __str__(self):
        print(f'Автомобиль: (цвет= {self.color}, количество пассажирских мест={self.count_passenger_seats},\
наличие десткого кресла={self.is_baby_seat},  в работе={self.is_busy})')
        #pass




class Taxi:
    def __init__(self,  *args):
        self.cars = args
        #print(cars)

    def find_car(self, count_passenger_seats, is_baby_seat):
        self.exist_car=0
        for i in self.cars:
            if int(i.count_passenger_seats) >= int(count_passenger_seats) \
                    and int(i.is_baby_seat)>=int(is_baby_seat) \
                    and int(i.is_busy) == 0:
                self.exist_car = 1
                i.__str__()
                print("Переводим в: ")
                i.is_busy = 1
                return(i.__str__())
            if self.exist_car==0:
                print('None')
                return ('None')








car1 = Car('Белый', '4', '2', '0')
#car1.__str__()
car2 = Car('Синий', '3', '1', '1')
#car2.__str__()

taxi = Taxi(car1, car2)
taxi.find_car(1,1)
