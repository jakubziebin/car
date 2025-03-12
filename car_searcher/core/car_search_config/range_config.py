from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass


@dataclass
class CarRangesConfig:
    """Config class for car_searcher search ranges."""

    min_year: int | None = None
    max_year: int = datetime.now().year
    max_price: int | None = None
    min_capacity: int | None = None
    max_capacity: int | None = None
    min_mileage: int | None = None
    max_mileage: int | None = None
    min_power: int | None = None
    max_power: int | None = None
