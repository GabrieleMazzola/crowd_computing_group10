from enum import IntEnum


class Satisfaction(IntEnum):
    VERY_WEAK = 1,
    WEAK = 2,
    INDIFFERENT = 3,
    MEDIUM = 4,
    STRONG = 5,
    VERY_STRONG = 6

    def __str__(self):
        return str(self.value)
