from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By

from car.core.olx.constants import LOCATION_INPUT_ID_OLX
from car.utils.stale_element_handle import StaleElementHandler

if TYPE_CHECKING:
    from selenium.webdriver import Chrome


class OlxLocationSetter:
    def __init__(self, webdriver: Chrome, city: str):
        """
        Initialize `OlxLocationSetter`.

        Args:
            webdriver: chrome webdriver.
            city: city to search car in.
        """

        self._webdriver = webdriver
        self._city = city.capitalize()

    def execute_location_set(self) -> None:
        self.paste_city_to_the_input()
        StaleElementHandler(self.choose_location_from_expanded_list).execute()

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
