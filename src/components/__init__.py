from enum import Enum, unique
from typing import NamedTuple


@unique
class State(Enum):
    """
    active: currently in stock
    inactive: out of stock
    """

    active = "active"
    inactive = "inactive"


class Item(NamedTuple):
    id: str
    price: float
    state: State
