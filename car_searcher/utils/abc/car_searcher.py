from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver


class BaseCarSearcher(ABC):
    """Base class for car_searcher searchers (pasting car_searcher model to the input etc.)."""

    def __init__(self, webdriver: WebDriver) -> None:
        self._webdriver = webdriver

    @abstractmethod
    def execute_car_search(self) -> None:
        """Method to execute searching of the car_searcher."""

    @property
    def webdriver(self) -> WebDriver:
        return self._webdriver
