from __future__ import annotations

import contextlib
import time
from typing import TYPE_CHECKING, Final
from functools import partial

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from car.core.olx.constants.timeouts import WAIT_BETWEEN_FIELDS_SETTING
from car.utils.abc.car_searcher import BaseCarSearcher
from car.utils.stale_element_handle import StaleElementHandler
from car.core.olx.constants import (
    SEARCH_INPUT_ID_OLX,
    CAR_TO_CHOOSE_CLASS_OLX,
    DEFAULT_WAIT_TIMEOUT,
    MODEL_CHOOSE_OLX_XPATH,
)
from car.core.olx.constants.xpaths import (
    ALL_CATEGORIES_OLX_XPATH,
    CATEGORY_DROPDOWN_OLX_XPATH,
    MOTORIZATION_OLX_XPATH,
    CAR_CATEGORY_OLX_XPATH,
)

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.remote.webelement import WebElement


class CarSearcher(BaseCarSearcher):
    """Class used to search car on OLX."""

    TIMEOUT_AFTER_ACTION: Final[float] = WAIT_BETWEEN_FIELDS_SETTING

    def __init__(self, webdriver: WebDriver, car_brand: str, car_model: str) -> None:
        """
        Initialize CarSearcher.

        Args:
            webdriver: webdriver.
            car_brand: brand of the car.
            car_model: model of the car.
        """
        super().__init__(webdriver)
        self._car_brand = car_brand
        self._car_model = car_model

    def execute_car_search(self) -> None:
        self.paste_car_model_in_input()
        self.confirm_search_olx()
        self.click_category_dropdown()
        self.set_category()
        self.expand_car_models_list()
        self.select_passed_model_from_expanded_list()

    def paste_car_model_in_input(self) -> None:
        """Paste car model in the search input."""
        input_component = self.webdriver.find_element(By.ID, SEARCH_INPUT_ID_OLX)
        input_component.send_keys(f"{self._car_brand} {self._car_model}")

    def confirm_search_olx(self) -> None:
        self.webdriver.find_element(By.ID, SEARCH_INPUT_ID_OLX).submit()

    def click_category_dropdown(self) -> None:
        """Click of the dropdown with categories to choose."""
        WebDriverWait(self.webdriver, DEFAULT_WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, CATEGORY_DROPDOWN_OLX_XPATH))
        )
        category_dropdown = self.webdriver.find_element(
            By.XPATH, CATEGORY_DROPDOWN_OLX_XPATH
        )

        with contextlib.suppress(
            NoSuchElementException
        ):  # Category is already set when exception occurred,
            category_dropdown.find_element(By.XPATH, ALL_CATEGORIES_OLX_XPATH)
            category_dropdown.click()

    def set_category(self) -> None:
        """Set motorization category."""
        motorization_choose = self.webdriver.find_element(
            By.XPATH, MOTORIZATION_OLX_XPATH
        )
        actions = ActionChains(self.webdriver)
        actions.move_to_element(motorization_choose).perform()

        car_item = self.webdriver.find_element(By.XPATH, CAR_CATEGORY_OLX_XPATH)
        car_item.click()
        time.sleep(self.TIMEOUT_AFTER_ACTION)

    def expand_car_models_list(self) -> None:
        def click_car_list() -> bool:
            self.webdriver.find_element(By.XPATH, MODEL_CHOOSE_OLX_XPATH).click()
            return True

        WebDriverWait(self.webdriver, DEFAULT_WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, MODEL_CHOOSE_OLX_XPATH))
        )
        StaleElementHandler(click_car_list).execute()
        time.sleep(self.TIMEOUT_AFTER_ACTION)

    def select_passed_model_from_expanded_list(self) -> None:
        def click_chosen_model(cars: list[WebElement]) -> bool:
            for car in cars:
                try:
                    p_element = car.find_element(By.TAG_NAME, "p")
                    if p_element.text == self._car_model.capitalize():
                        car.click()
                        return True
                except NoSuchElementException:
                    continue

            return False

        car_list = self.webdriver.find_element(By.XPATH, MODEL_CHOOSE_OLX_XPATH)

        cars_to_choose = car_list.find_elements(By.CLASS_NAME, CAR_TO_CHOOSE_CLASS_OLX)
        StaleElementHandler(partial(click_chosen_model, cars=cars_to_choose)).execute()

        car_list.click()  # close car list
        time.sleep(self.TIMEOUT_AFTER_ACTION)
