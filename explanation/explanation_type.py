from enum import Enum


class ExplanationType(Enum):
    # fully anonymous without numbers
    ANONYMOUS = 1
    # anonymous with numbers
    ANONYMOUS_GROUP = 2
    # close person only
    PERSON_ONLY = 3
    #close person + group
    PERSON_GROUP = 4

