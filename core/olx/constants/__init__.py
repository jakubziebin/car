from __future__ import annotations

from .paths import CHROME_DRIVER_PATH
from .urls import OLX_URL
from .xpaths import (
    MODEL_CHOOSE_OLX_XPATH,
    CATEGORY_DROPDOWN_OLX_XPATH,
    ALL_CATEGORIES_OLX_XPATH,
    MOTORIZATION_OLX_XPATH,
    CAR_CATEGORY_OLX_XPATH,
    FROM_PRODUCTION_YEAR_OLX_XPATH,
    TO_PRODUCTION_YEAR_OLX_XPATH,
    FROM_ENGINE_CAPACITY_OLX_XPATH,
    FUEL_TYPE_DROPDOWN_OLX_XPATH,
    TO_ENGINE_CAPACITY_OLX_XPATH,
    MIN_MILEAGE_INPUT_OLX_XPATH,
    MAX_MILEAGE_INPUT_OLX_XPATH,
    MIN_POWER_INPUT_OLX_XPATH,
    MAX_POWER_INPUT_OLX_XPATH,
    DRIVE_TYPE_DROPDOWN_OLX_XPATH,
    GEARBOX_TYPE_DROPDOWN_OLX_XPATH,
    BODY_TYPE_DROPDOWN_OLX_XPATH,
    PRODUCTION_COUNTRY_DROPDOWN_OLX_XPATH,
    CAR_COLOR_DROPDOWN_OLX_XPATH,
    CAR_STEERING_WHEEL_PLACEMENT_DROPDOWN_OLX_XPATH,
    CAR_TECHNICAL_CONDITION_DROPDOWN_OLX_XPATH,
    LOCATION_BUTTON_OLX_XPATH,
)
from .element_names import MAX_PRICE_INPUT_NAME_OLX
from .element_ids import (
    CONFIRM_PRIVACY_TERMS_BUTTON_ID_OLX,
    SEARCH_INPUT_ID_OLX,
    LOCATION_INPUT_ID_OLX,
)
from .element_classes import CAR_TO_CHOOSE_CLASS_OLX
from .timeouts import DEFAULT_WAIT_TIMEOUT


__all__ = [
    # PATHS
    "CHROME_DRIVER_PATH",
    # URLS
    "OLX_URL",
    # ELEMENT IDS
    "CONFIRM_PRIVACY_TERMS_BUTTON_ID_OLX",
    "SEARCH_INPUT_ID_OLX",
    "LOCATION_INPUT_ID_OLX",
    # ELEMENT CLASSES
    "CAR_TO_CHOOSE_CLASS_OLX",
    # ELEMENT NAMES
    "MAX_PRICE_INPUT_NAME_OLX",
    # TIMEOUTS
    "DEFAULT_WAIT_TIMEOUT",
    # XPATH
    "MODEL_CHOOSE_OLX_XPATH",
    "CATEGORY_DROPDOWN_OLX_XPATH",
    "ALL_CATEGORIES_OLX_XPATH",
    "MOTORIZATION_OLX_XPATH",
    "CAR_CATEGORY_OLX_XPATH",
    "FROM_PRODUCTION_YEAR_OLX_XPATH",
    "TO_PRODUCTION_YEAR_OLX_XPATH",
    "FROM_ENGINE_CAPACITY_OLX_XPATH",
    "FUEL_TYPE_DROPDOWN_OLX_XPATH",
    "TO_ENGINE_CAPACITY_OLX_XPATH",
    "MIN_MILEAGE_INPUT_OLX_XPATH",
    "MAX_MILEAGE_INPUT_OLX_XPATH",
    "MAX_POWER_INPUT_OLX_XPATH",
    "MIN_POWER_INPUT_OLX_XPATH",
    "DRIVE_TYPE_DROPDOWN_OLX_XPATH",
    "GEARBOX_TYPE_DROPDOWN_OLX_XPATH",
    "BODY_TYPE_DROPDOWN_OLX_XPATH",
    "PRODUCTION_COUNTRY_DROPDOWN_OLX_XPATH",
    "CAR_COLOR_DROPDOWN_OLX_XPATH",
    "CAR_STEERING_WHEEL_PLACEMENT_DROPDOWN_OLX_XPATH",
    "CAR_TECHNICAL_CONDITION_DROPDOWN_OLX_XPATH",
    "LOCATION_BUTTON_OLX_XPATH",
]
