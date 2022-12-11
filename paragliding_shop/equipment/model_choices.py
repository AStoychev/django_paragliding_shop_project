from enum import Enum

from paragliding_shop.accounts.models import ChoicesEnumMixin


class WingsCertificationChoices(ChoicesEnumMixin, Enum):
    EN_A = "EN A"
    EN_B = "EN B"
    EN_C = "EN C"
    EN_D = "EN D"
    Tandem = "Tandem wings"
    Acro = "Acro wings"
    Speedwings = "Speedwings"


class WingTestChoices(ChoicesEnumMixin, Enum):
    Yes = "Yes"
    No = "No"


class HarnessCategoryChoices(ChoicesEnumMixin, Enum):
    Standard = "Standard"
    Reversible = "Reversible"
    Mountain = "Mountain"
    Pod = "Pod"
    Acro = "Acro"
    Speed_Flying = "Speed Flying"
    Tandem = "Tandem"


class ReservesTypeChoices(ChoicesEnumMixin, Enum):
    Standard = "Standard"
    Light = "Light"


class InstrumentsChoices(ChoicesEnumMixin, Enum):
    Varios = "Varios"
    AltiVarios = "AltiVarios"
    AltiVariosGPS = "AltiVariosGPS"


class HelmetVisorChoices(ChoicesEnumMixin, Enum):
    Yes = "Yes"
    No = "No"


class ConditionChoices(ChoicesEnumMixin, Enum):
    New = "New"
    Used = "Used"
