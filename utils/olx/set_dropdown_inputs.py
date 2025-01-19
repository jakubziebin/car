from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from selenium.webdriver.common.by import By

from car.exceptions.car_exception import CarException
from car.core.olx.constants.xpaths import FUEL_TYPE_DROPDOWN_OLX_XPATH
from car.core.olx.constants import (
    DRIVE_TYPE_DROPDOWN_OLX_XPATH,
    GEARBOX_TYPE_DROPDOWN_OLX_XPATH,
    BODY_TYPE_DROPDOWN_OLX_XPATH,
)
from car.core.olx.options_to_choose.car_attributes import (
    CarPossibleFuelOlx,
    CarPossibleDriveOlx,
    CarPossibleGearboxOlx,
    CarPossibleBodyOlx,
)

if TYPE_CHECKING:
    from selenium.webdriver import Chrome


DropdownPossibleChooses = TypeVar(
    "DropdownPossibleChooses",
    bound=CarPossibleDriveOlx
    | CarPossibleFuelOlx
    | CarPossibleGearboxOlx
    | CarPossibleBodyOlx,
)


class DropdownOptionsError(CarException):
    """Base class for exceptions in the dropdown options."""


class DropdownOptionsAllWithOthersError(DropdownOptionsError):
    """Exception raised for choosing 'Wszystkie' option with others."""

    def __init__(self) -> None:
        self.message = "Cannot choose 'Wszystkie' option with others."
        super().__init__(self.message)


def _set_dropdown_options(
    webdriver: Chrome,
    dropdown_xpath: str,
    *dropdown_chooses: DropdownPossibleChooses,
) -> None:
    """
    Common function to set dropdown options.

    Args:
        webdriver (Chrome): Selenium webdriver.
        dropdown_xpath (str): XPath to the dropdown.
        dropdown_chooses (DropdownPossibleChooses): Dropdown options to choose.

    Raises:
        DropdownOptionsAllWithOthersError: If 'Wszystkie' option is in dropdown_chooses and there are other options.
    """
    if len(dropdown_chooses) > 1 and "Wszystkie" in dropdown_chooses:
        raise DropdownOptionsAllWithOthersError

    dropdown = webdriver.find_element(By.XPATH, dropdown_xpath)
    dropdown.click()

    options_to_choose = dropdown.find_elements(By.TAG_NAME, "p")

    for option in options_to_choose:
        if option.text not in dropdown_chooses:
            continue
        option.click()

    dropdown.click()  # Close dropdown after choosing options.


def set_fuel_type_olx(webdriver: Chrome, *fuel_types: CarPossibleFuelOlx) -> None:
    """
    Set fuel type in the dropdown on the OLX website.

    Args:
        webdriver (Chrome): Selenium webdriver.
        fuel_types (CarPossibleFuelOlx): Fuel types to choose.
    """
    _set_dropdown_options(webdriver, FUEL_TYPE_DROPDOWN_OLX_XPATH, *fuel_types)


def set_drive_type_olx(webdriver: Chrome, *drive_types: CarPossibleDriveOlx) -> None:
    """
    Set drive type in the dropdown on the OLX website.

    Args:
        webdriver (Chrome): Selenium webdriver.
        drive_types (CarPossibleDriveOlx): Drive types to choose.
    """
    _set_dropdown_options(webdriver, DRIVE_TYPE_DROPDOWN_OLX_XPATH, *drive_types)


def set_gearbox_type_olx(
    webdriver: Chrome, *gearbox_types: CarPossibleGearboxOlx
) -> None:
    """
    Set gearbox type in the dropdown on the OLX website.

    Args:
        webdriver (Chrome): Selenium webdriver.
        gearbox_types (CarPossibleGearboxOlx): Gearbox types to choose.
    """
    _set_dropdown_options(webdriver, GEARBOX_TYPE_DROPDOWN_OLX_XPATH, *gearbox_types)


def set_body_type_olx(webdriver: Chrome, *body_types: CarPossibleBodyOlx) -> None:
    """
    Set body type in the dropdown on the OLX website.

    Args:
        webdriver (Chrome): Selenium webdriver.
        body_types (CarPossibleBodyOlx): Body types to choose.
    """
    _set_dropdown_options(webdriver, BODY_TYPE_DROPDOWN_OLX_XPATH, *body_types)
