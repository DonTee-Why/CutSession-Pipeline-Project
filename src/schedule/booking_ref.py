from abc import ABC, abstractmethod
from datetime import datetime
import string
import secrets
from .schemas.bookings import BookingsCreateModel


class BookingRefStrategy(ABC):
    @abstractmethod
    def generate_booking_ref() -> None:
        pass


class RandomStrategy(BookingRefStrategy):
    def generate_booking_ref(self) -> str:
        limit = 9
        ref = "".join(secrets.choice(string.ascii_uppercase+string.digits)
                        for i in range(limit))
        return ref


class DerivedStrategy(BookingRefStrategy, BookingsCreateModel):
    # booking_id = "50b96d7e-e657-454d-908d-dd90d35d6a19"
    # date = "2023-02-23"
    def generate_booking_ref(self) -> str:
        booking_id = self.booking_id[-4:]
        date = datetime.strptime(self.date, "%Y-%m-%d")
        ref = "".join(["BK-", booking_id.upper(), str(date.day)])
        return ref


class BookingRef:
    strategy: BookingRefStrategy
    booking_ref: str

    def __init__(self, strategy: BookingRefStrategy) -> None:
        self.strategy = strategy

    def get_booking_ref(self) -> str:
        ref = self.strategy.generate_booking_ref()
        self.booking_ref = ref
        return self.booking_ref
