from __future__ import annotations

import time
from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from car.core.olx.constants import (
    LOCATION_INPUT_ID_OLX,
    LOCATION_BUTTON_OLX_XPATH,
    DEFAULT_WAIT_TIMEOUT,
)
from car.utils.stale_element_handle import StaleElementHandler

if TYPE_CHECKING:
    from selenium.webdriver import Chrome

    from car.core.olx.options_to_choose.possible_distance_from_location import (
        PossibleDistanceFromLocation,
    )


class OlxLocationSetter:
    def __init__(
        self,
        webdriver: Chrome,
        city: str,
        max_distance_from: PossibleDistanceFromLocation,
    ):
        """
        Initialize `OlxLocationSetter`.

        Args:
            webdriver: chrome webdriver.
            city: city to search car in.
        """

        self._webdriver = webdriver
        self._city = city.capitalize()
        self._max_distance_from = max_distance_from

    def execute_location_set(self) -> None:
        self.paste_city_to_the_input()
        StaleElementHandler(self.choose_location_from_expanded_list).execute()
        StaleElementHandler(self.set_max_distance_from).execute()

    def paste_city_to_the_input(self) -> None:
        """Paste given city to the location input."""
        location_input = self._webdriver.find_element(By.ID, LOCATION_INPUT_ID_OLX)
        location_input.send_keys(self._city)

    def choose_location_from_expanded_list(self) -> bool:
        """
        Choose city from the expanded list.

        This method is used in `StaleElementHandler`, that's the reason why it returns bool.


        Returns:
            bool: True -> if location was found and clicked, False otherwise.
        """

        suggestions = self._webdriver.find_elements(By.TAG_NAME, "li")

        for suggestion in suggestions:
            if self._city in suggestion.text:
                suggestion.click()
                return True
        return False

    def set_max_distance_from(self) -> bool:
        """Set maximum distance from the selected location."""
        WebDriverWait(self._webdriver, DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, LOCATION_BUTTON_OLX_XPATH))
        ).click()

        options = self._webdriver.find_elements(
            By.XPATH, "//span[@data-testid='dropdown-item-text']"
        )

        for option in options:
            if option.text == self._max_distance_from:
                time.sleep(1)
                option.click()
                return True
        return False
