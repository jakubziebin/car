from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from car.core.olx.constants import (
    DEFAULT_WAIT_TIMEOUT,
    MAX_PRICE_INPUT_NAME_OLX,
    FROM_PRODUCTION_YEAR_OLX_XPATH,
    TO_PRODUCTION_YEAR_OLX_XPATH,
    FROM_ENGINE_CAPACITY_OLX_XPATH,
    TO_ENGINE_CAPACITY_OLX_XPATH,
    MIN_MILEAGE_INPUT_OLX_XPATH,
    MAX_MILEAGE_INPUT_OLX_XPATH,
    MIN_POWER_INPUT_OLX_XPATH,
    MAX_POWER_INPUT_OLX_XPATH,
)

if TYPE_CHECKING:
    from selenium.webdriver import Chrome


def _set_range_inputs_value(
    webdriver: Chrome,
    min_input_xpath: str,
    max_input_x_path: str,
    *,
    min_value: int | None = None,
    max_value: int | None = None,
) -> None:
    """Function to set value of inputs with min and max value."""
    if min_value is not None:
        min_value_input = webdriver.find_element(By.XPATH, min_input_xpath)
        min_value_input.send_keys(str(min_value))

    if max_value is not None:
        max_value_input = webdriver.find_element(By.XPATH, max_input_x_path)
        max_value_input.send_keys(str(max_value))


def set_max_price_olx(webdriver: Chrome, max_price: int) -> None:
    """Wait for max price input to be present and set the max price."""

    WebDriverWait(webdriver, DEFAULT_WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.NAME, MAX_PRICE_INPUT_NAME_OLX))
    )

    max_price_input = webdriver.find_element(By.NAME, MAX_PRICE_INPUT_NAME_OLX)
    max_price_input.send_keys(str(max_price))


def set_production_year_fork_olx(
    webdriver: Chrome, *, from_year: int, to_year: int
) -> None:
    """Set min and max production year of the car."""
    _set_range_inputs_value(
        webdriver,
        FROM_PRODUCTION_YEAR_OLX_XPATH,
        TO_PRODUCTION_YEAR_OLX_XPATH,
        min_value=from_year,
        max_value=to_year,
    )


def set_engine_capacity_olx(
    webdriver: Chrome,
    *,
    from_capacity: int | None = None,
    to_capacity: int | None = None,
) -> None:
    """Set min and max engine capacity of the car."""
    _set_range_inputs_value(
        webdriver,
        FROM_ENGINE_CAPACITY_OLX_XPATH,
        TO_ENGINE_CAPACITY_OLX_XPATH,
        min_value=from_capacity,
        max_value=to_capacity,
    )


def set_car_mileage_olx(
    webdriver: Chrome,
    *,
    min_mileage: int | None = None,
    max_mileage: int | None = None,
) -> None:
    """Set min and max mileage of the searched car."""
    _set_range_inputs_value(
        webdriver,
        MIN_MILEAGE_INPUT_OLX_XPATH,
        MAX_MILEAGE_INPUT_OLX_XPATH,
        min_value=min_mileage,
        max_value=max_mileage,
    )


def set_engine_power_olx(
    webdriver: Chrome,
    *,
    min_power: int | None = None,
    max_power: int | None = None,
) -> None:
    """Set min and max power of the engine."""
    _set_range_inputs_value(
        webdriver,
        MIN_POWER_INPUT_OLX_XPATH,
        MAX_POWER_INPUT_OLX_XPATH,
        min_value=min_power,
        max_value=max_power,
    )
