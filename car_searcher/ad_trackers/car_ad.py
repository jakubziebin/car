from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime


@dataclass
class CarAd:
    id: str
    title: str
    price: int
    url: str
    location: str
    date_found: datetime
