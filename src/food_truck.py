from dataclasses import dataclass

from typing import Dict


@dataclass
class FoodTruck:
    data: Dict

    @property
    def name(self) -> str:
        return self.data.get("applicant")

    @property
    def address(self) -> str:
        return self.data.get("location")
