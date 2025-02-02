from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from car.core.car_search_config.range_config import CarRangesConfig
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
from car.utils.abc.range_inputs_setter import RangeInputsSetter

if TYPE_CHECKING:
    from selenium.webdriver import Chrome


class OlxRangeInputsSetter(RangeInputsSetter):
    def __init__(self, webdriver: Chrome, car_ranges_config: CarRangesConfig) -> None:
        """
        Initialize OlxRangeInputsSetter.

        Args:
            webdriver: Chrome webdriver.
            car_ranges_config: car ranges config instance.
        """
        super().__init__(webdriver=webdriver)
        self._config = car_ranges_config

    def execute_range_inputs_filling(self) -> None:
        self.set_production_year_fork()
        self.set_max_price()
        self.set_engine_capacity()
        self.set_car_mileage()
        self.set_engine_power()

    def set_production_year_fork(self) -> None:
        self.set_range_inputs_value(
            FROM_PRODUCTION_YEAR_OLX_XPATH,
            TO_PRODUCTION_YEAR_OLX_XPATH,
            min_value=self._config.min_year,
            max_value=self._config.max_year,
        )

    def set_max_price(self) -> None:
        WebDriverWait(self.webdriver, DEFAULT_WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.NAME, MAX_PRICE_INPUT_NAME_OLX))
        )

        max_price_input = self.webdriver.find_element(By.NAME, MAX_PRICE_INPUT_NAME_OLX)
        max_price_input.send_keys(str(self._config.max_price))

    def set_engine_capacity(self) -> None:
        self.set_range_inputs_value(
            FROM_ENGINE_CAPACITY_OLX_XPATH,
            TO_ENGINE_CAPACITY_OLX_XPATH,
            min_value=self._config.min_capacity,
            max_value=self._config.max_capacity,
        )

    def set_car_mileage(self) -> None:
        self.set_range_inputs_value(
            MIN_MILEAGE_INPUT_OLX_XPATH,
            MAX_MILEAGE_INPUT_OLX_XPATH,
            min_value=self._config.min_mileage,
            max_value=self._config.max_mileage,
        )

    def set_engine_power(self) -> None:
        self.set_range_inputs_value(
            MIN_POWER_INPUT_OLX_XPATH,
            MAX_POWER_INPUT_OLX_XPATH,
            min_value=self._config.min_power,
            max_value=self._config.max_power,
        )
