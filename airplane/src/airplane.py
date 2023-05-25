import time

from seats import CheapSeat, BusinessSeat, FirstSeat
from const import DEFAULT_FLIGHT_DURATION, SeatCategory


class Heater:
    def __init__(self):
        pass

    def begin_heating(self):
        pass


class Kitchen:
    def __init__(self, meals: dict):
        self.meals = meals
        self.flight_in_progress = False
        self.heat = Heater()

    def start_delivery(self):
        print("Пора обедать!")

    def start_flight(self):
        self.flight_in_progress = True
        print("Летим!")

    def end_flight(self):
        self.flight_in_progress = False
        print("Не летим!")

    def begin_heating(self):
        """
        Включает разогрев.
        :return:
        """
        self.heat.begin_heating()
        print("Начали разогрев")


class Flight:
    def __init__(self):
        self.flight_in_progress = False
        self.autopilot_enabled = False

    def start(self):
        self.flight_in_progress = True
        print("Взлетаем!")

    def land(self):
        self.flight_in_progress = False
        print("Приземляемся!")

    def enable_autopilot(self, destination: tuple[int]):
        self.autopilot_enabled = True
        print(f"Автопилот включён. Точка назначения: {destination}")

    def disable_autopilot(self):
        self.autopilot_enabled = False
        print("Автопилот выключен")

    def flight_indication(self, duration: int):
        timestamp = time.time() + duration
        start_time = time.time()
        while timestamp > time.time():
            time.sleep(1)
            print(f"Полёт в процессе уже {int(time.time() - start_time)} секунд")


class Airplane:
    weight = 40

    def __init__(self, colour):
        self._colour = colour
        self._on_flight = False
        self._passengers = 0
        self.flight = Flight()
        self.cheap_class_seats: dict = dict()
        self.businnes_class_seats: dict = dict()
        self.first_class_seats: dict = dict()
        self._create_seats()

    def _create_seats(self):
        for number in range(1, 201):
            self.cheap_class_seats[number] = CheapSeat(SeatCategory.econom, number)
        for number in range(1, 51):
            self.businnes_class_seats[number] = BusinessSeat(SeatCategory.business, number)
        for number in range(1, 11):
            self.first_class_seats[number] = FirstSeat(SeatCategory.first, number)

    def fasten_single_belt(self, seat_type: str, number: int):
        if seat_type == SeatCategory.econom:
            self.cheap_class_seats[number].fasten_belt()
        elif seat_type == SeatCategory.business:
            self.businnes_class_seats[number].fasten_belt()
        elif seat_type == SeatCategory.first:
            self.first_class_seats[number].fasten_belt()
        else:
            print("Unknown seat type!")

    def fasten_all_belts(self):
        for seat_dict in (self.cheap_class_seats, self.businnes_class_seats, self.first_class_seats):
            for value in seat_dict.values():
                value.fasten_belt()
        self.show_message("Пристегните ремни!")

    def loose_all_belts(self):
        for seat_dict in (self.cheap_class_seats, self.businnes_class_seats, self.first_class_seats):
            for value in seat_dict.values():
                value.loose_belt()
        self.show_message("Ремни отстёгнуты!")

    def start_flight(self, aeroport_coords, duration=DEFAULT_FLIGHT_DURATION):
        self.fasten_all_belts()
        self.flight.start()
        self.flight.enable_autopilot(aeroport_coords)
        self.show_message("Полёт начинается!")
        self.flight.flight_indication(duration)

    def finish_flight(self):
        self.flight.disable_autopilot()
        self.flight.land()
        self.loose_all_belts()
        self.show_message("Полёт завершён")

    def move(self, coords, duration=DEFAULT_FLIGHT_DURATION):
        self.start_flight(coords, duration=duration)
        self.finish_flight()

    def set_passengers(self, count):
        self._passengers = count

    def get_passengers(self):
        return self._passengers

    def show_message(self, text):
        print(text)

    def call_earth(self):
        if self._on_flight:
            print("Calling...")
        else:
            print("Please disable your cell phones!")

    def is_on_flight(self, condition: bool):
        self._on_flight = condition

    def print_parameters(self):
        print(self.weight)
        print(self._colour)

    def __eq__(self, other):
        return self._passengers == other.get_passengers()

    def __lt__(self, other):
        return self._passengers < other.get_passengers()

    def __gt__(self, other):
        return self._passengers > other.get_passengers()


if __name__ == "__main__":
    pass
