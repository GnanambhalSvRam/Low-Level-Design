from enum import Enum

class STATUS(Enum):
    PENDING = 1
    CONFIRMED = 2
    PREPARING = 3
    ON_THE_WAY = 4
    DELIVERED = 5
    CANCELLED = 6