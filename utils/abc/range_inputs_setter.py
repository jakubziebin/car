from __future__ import annotations

import time
from typing import ClassVar
from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class RangeInputsSetter(ABC):
    """Base class for setting range inputs."""

    TIMEOUT_BETWEEN_RANGES_SET: ClassVar[int] = 1

    def __init__(self, webdriver: WebDriver) -> None:
        self._webdriver = webdriver

    @abstractmethod
    def execute_range_inputs_filling(self) -> None:
        """
        Method to execute filling range inputs.

        Please notice that to use this setter you need to create and instance end then execute this method.
        """

    @property
    def webdriver(self) -> WebDriver:
        return self._webdriver

    def set_range_inputs_value(
        self,
        min_input_xpath: str,
        max_input_x_path: str,
        *,
        min_value: int | None = None,
        max_value: int | None = None,
        timeout: float | int | None = None,
    ) -> None:
        """
        Method to set value of inputs with min and max value.

        Args:
            min_input_xpath(str): xpath to min input.
            max_input_x_path(str): xpath to max input.
            min_value(int | None): value to set in min input.
            max_value(int | None): value to set in max input.
            timeout(int | float | None): wait after setting inputs.

        Raises:
            ValueError: If min_value is greater than max_value.
            AssertionError: If min_value and max_value are None.
        """
        assert min_value is not None or max_value is not None, (
            "Both min and max values cannot be None."
        )

        if (min_value is not None and max_value is not None) and min_value > max_value:
            raise ValueError("Min value cannot be greater than max value.")

        if min_value is not None:
            min_value_input = self.webdriver.find_element(By.XPATH, min_input_xpath)
            min_value_input.send_keys(str(min_value))
            time.sleep(self.TIMEOUT_BETWEEN_RANGES_SET)

        if max_value is not None:
            max_value_input = self.webdriver.find_element(By.XPATH, max_input_x_path)
            max_value_input.send_keys(str(max_value))
            time.sleep(self.TIMEOUT_BETWEEN_RANGES_SET)

        if timeout is not None:
            time.sleep(timeout)
