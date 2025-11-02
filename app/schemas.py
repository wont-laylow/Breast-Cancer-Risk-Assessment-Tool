from pydantic import BaseModel
from enum import Enum


class Age(str, Enum):
    BELOW_35 = "<35"
    BETWEEN_35_44 = "35-44"
    BETWEEN_45_54 = "45-54"
    ABOVE_55 = "≥55"
    UNKNOWN = "Unknown"


class Education(str, Enum):
    JUNIOR_SECONDARY = "Junior secondary school"
    PRIMARY = "Primary school"
    SENIOR_OR_HIGHER = "≥ Senior secondary school"
    UNKNOWN = "Unknown"
    NO_FORMAL = "No formal education"


class FamilyHistory(str, Enum):
    NO = "No"
    YES = "Yes"
    UNKNOWN = "Unknown"


class Parity(str, Enum):
    NULLIPAROUS = "Nulliparous"
    ONE_TWO = "1-2"
    THREE_FOUR = "3-4"
    FIVE_OR_MORE = "≥5"
    UNKNOWN = "Unknown"


class MenarcheAge(str, Enum):
    UNDER_15 = "<15"
    FIFTEEN = "15"
    SIXTEEN = "16"
    SEVENTEEN_OR_ABOVE = "≥17"
    UNKNOWN = "Unknown"


class MenopauseAge(str, Enum):
    PREMENOPAUSAL = "Premenopausal"
    UNDER_45 = "<45"
    BETWEEN_45_49 = "45-49"
    BETWEEN_50_54 = "50-54"
    ABOVE_55 = "≥55"
    UNKNOWN = "Unknown"


class BodySize(str, Enum):
    SLIGHT = "Slight"
    AVERAGE = "Average"
    SLIGHTLY_HEAVY = "Slightly heavy"
    VERY_HEAVY = "Very heavy"
    UNKNOWN = "Unknown"


class PatientData(BaseModel):
    Age: Age
    Education: Education
    Family_History: FamilyHistory
    Parity: Parity
    Menarche_Age: MenarcheAge
    Menopause_Age: MenopauseAge
    Body_Size: BodySize
