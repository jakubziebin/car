from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable

from selenium.webdriver.common.by import By

from car.exceptions.car_exception import CarException
from car.core.car_search_config.car_properties_config import BaseCarPropertiesConfig

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver


class DropdownOptionsError(CarException):
    """Base class for exceptions in the dropdown options."""


class DropdownOptionsAllWithOthersError(DropdownOptionsError):
    """Exception raised for choosing 'Wszystkie' option with others."""

    def __init__(self) -> None:
        self.message = "Cannot choose 'Wszystkie' option with others."
        super().__init__(self.message)


class BaseDropdownInputsSetter(ABC):
    """Base class for dropdown inputs setter."""

    def __init__(
        self,
        webdriver: WebDriver,
        car_properties_config: BaseCarPropertiesConfig,
    ) -> None:
        self._webdriver = webdriver
        self._config = car_properties_config

    @abstractmethod
    def execute_dropdown_inputs_set(self) -> None:
        """Method to execute setting of dropdown inputs."""

    @property
    def webdriver(self) -> WebDriver:
        return self._webdriver

    @property
    def config(self) -> BaseCarPropertiesConfig:  # override me to have proper type.
        return self._config

    def set_dropdown_options(
        self,
        dropdown_xpath: str,
        *dropdown_chooses: Iterable[str],
    ) -> None:
        """
        Common function to set dropdown options.

        Args:
            dropdown_xpath (str): XPath to the dropdown.
            dropdown_chooses (DropdownPossibleChoosesT): Dropdown options to choose.

        Raises:
            DropdownOptionsAllWithOthersError: If 'Wszystkie' option is in dropdown_chooses and there are other options.
        """
        if len(dropdown_chooses) > 1 and "Wszystkie" in dropdown_chooses:
            raise DropdownOptionsAllWithOthersError

        dropdown = self.webdriver.find_element(By.XPATH, dropdown_xpath)
        dropdown.click()

        options_to_choose = dropdown.find_elements(By.TAG_NAME, "p")

        for option in options_to_choose:
            if option.text not in dropdown_chooses:
                continue
            option.click()

        dropdown.click()  # Close dropdown after choosing options.
