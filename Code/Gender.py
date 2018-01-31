from enum import Enum, unique, auto

@unique
class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
    GENDERLESS = auto()
