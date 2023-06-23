from components import Item


class Buffer(object):
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and
    LIFO (Last In First Out).
    """

    def __init__(self, policy: str):
        policy = policy.upper()
        if policy not in ["FIFO", "LIFO"]:
            raise ValueError()
        self._policy = policy


    def insert(self, item: Item) -> None:
        # TODO: Put your code here
        # ...
        raise NotImplementedError

    def extract(self) -> Item:
        # TODO: Put your code here
        # ...
        raise NotImplementedError

    def flush(self) -> None:
        # TODO: Put your code here
        # ...
        raise NotImplementedError
