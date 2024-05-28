from random import randint


class Format:
    @classmethod
    def add_extra_spaces(cls, data: str) -> str:
        return cls._random_spaces() + data + cls._random_spaces()

    @staticmethod
    def _random_spaces() -> str:
        return ' ' * randint(1, 10)
