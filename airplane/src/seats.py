class Seat:
    def __init__(self, category, number):
        self.category = category
        self.number = number
        self.belt_fastened = False

    def fasten_belt(self):
        self.belt_fastened = True
        print(f"Кресло категории {self.category}, №{self.number}: ремень пристёгнут")

    def loose_belt(self):
        self.belt_fastened = False
        print(f"Кресло категории {self.category}, №{self.number}: ремень отстёгнут")


class CheapSeat(Seat):
    def __init__(self, *args):
        super().__init__(*args)


class BusinessSeat(Seat):
    def enable_screen(self):
        print("Включили экран")

    def lower_spinka(self):
        print("Спинка откинута")


class FirstSeat(BusinessSeat):
    def enable_massage(self):
        print("Массаж включён")

    def lower_spinka(self):
        print("Спинка откинута и подножка выдвинута")


if __name__ == "__main__":
    seat1 = FirstSeat("aaa", 5)
    print(hasattr(seat1, "fasten_belt"))
    print(hasattr(seat1, "enable_screen"))