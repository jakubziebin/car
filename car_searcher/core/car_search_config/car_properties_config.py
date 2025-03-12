from __future__ import annotations

from dataclasses import dataclass
from abc import ABC


@dataclass
class BaseCarPropertiesConfig(ABC):
    """
    Base class for configuration of the car_searcher properties

    As each portal has different names for etc. fuel types, it is impossible to create config with identical
    field types for every portal.
    """
