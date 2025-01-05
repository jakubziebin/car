from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from car.car.core.constants import CONFIRM_PRIVACY_TERMS_BUTTON_ID, DEFAULT_WAIT_TIMEOUT

if TYPE_CHECKING:
    from selenium.webdriver import Chrome


def confirm_olx_privacy_terms(webdriver: Chrome) -> None:
    """Confirm privacy tems when entering OLX."""
    WebDriverWait(webdriver, DEFAULT_WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.ID, CONFIRM_PRIVACY_TERMS_BUTTON_ID))
    )
    webdriver.find_element(By.ID, CONFIRM_PRIVACY_TERMS_BUTTON_ID).click()
