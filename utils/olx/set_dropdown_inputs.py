from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By

from car.core.olx.constants.xpaths import FUEL_TYPE_DROPDOWN_OLX_XPATH

if TYPE_CHECKING:
    from selenium.webdriver import Chrome

    from car.core.olx.options_to_choose.car_attributes import CarPossibleFuelOlx


def set_fuel_type_olx(webdriver: Chrome, *fuel_types: CarPossibleFuelOlx) -> None:
    """
    Set fuel type in the dropdown on the OLX website.

    Args:
        webdriver (Chrome): Selenium webdriver.
        fuel_types (CarPossibleFuelOlx): Fuel types to choose.
    """
    fuel_dropdown = webdriver.find_element(By.XPATH, FUEL_TYPE_DROPDOWN_OLX_XPATH)
    fuel_dropdown.click()

    fuels_to_choose = fuel_dropdown.find_elements(By.TAG_NAME, "p")

    for fuel in fuels_to_choose:
        if fuel.text not in fuel_types:
            continue
        fuel.click()
