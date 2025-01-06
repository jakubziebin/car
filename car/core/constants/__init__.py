from __future__ import annotations

from .paths import CHROME_DRIVER_PATH
from .urls import OLX_URL
from .xpaths import MODEL_CHOOSE_OLX_XPATH
from .element_names import MAX_PRICE_INPUT_NAME_OLX
from .element_ids import CONFIRM_PRIVACY_TERMS_BUTTON_ID_OLX, SEARCH_INPUT_ID_OLX
from .timeouts import DEFAULT_WAIT_TIMEOUT


__all__ = [
    # PATHS
    "CHROME_DRIVER_PATH",
    # URLS
    "OLX_URL",
    # ELEMENT IDS
    "CONFIRM_PRIVACY_TERMS_BUTTON_ID_OLX",
    "SEARCH_INPUT_ID_OLX",
    # ELEMENT NAMES
    "MAX_PRICE_INPUT_NAME_OLX",
    # TIMEOUTS
    "DEFAULT_WAIT_TIMEOUT",
    # XPATH
    "MODEL_CHOOSE_OLX_XPATH",
]
