from typing import Tuple
from random import randint, uniform
from components import State


def generate_item() -> Tuple:
    def randomDigits(digits: int) -> int:
        lower = 10 ** (digits - 1)
        upper = 10**digits - 1
        return randint(lower, upper)

    retail_price = round(uniform(10.0, 100.0), 2)
    id = "MLX" + str(randomDigits(6))
    return (id, retail_price, State.active)
