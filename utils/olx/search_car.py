from __future__ import annotations

from typing import TYPE_CHECKING, Final

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    from selenium.webdriver import Chrome
    from selenium.webdriver.remote.webelement import WebElement


def paste_car_model_in_olx_search(
    webdriver: Chrome, car_brand: str, car_model: str
) -> None:
    input_component = webdriver.find_element(By.ID, SEARCH_INPUT_ID_OLX)
    input_component.send_keys(f"{car_brand} {car_model}")


def confirm_search_olx(webdriver: Chrome) -> None:
    webdriver.find_element(By.ID, SEARCH_INPUT_ID_OLX).submit()


def set_category_olx(webdriver: Chrome) -> None:
    """Wait for category input to be present and set the category (if not set before)."""

    category_dropdown = webdriver.find_element(By.XPATH, CATEGORY_DROPDOWN_OLX_XPATH)

    try:
        category_dropdown.find_element(By.XPATH, ALL_CATEGORIES_OLX_XPATH)
        category_dropdown.click()
    except NoSuchElementException:
        return  # Category is already set

    motorization_choose = webdriver.find_element(By.XPATH, MOTORIZATION_OLX_XPATH)
    actions = ActionChains(webdriver)
    actions.move_to_element(motorization_choose).perform()

    car_item = webdriver.find_element(By.XPATH, CAR_CATEGORY_OLX_XPATH)
    car_item.click()


def choose_car_model_olx(webdriver: Chrome, car_model: str) -> None:
    """Choose model car from the dropdown."""
    car_list: WebElement | None = None
    max_tries: Final[int] = 3
    current = 0

    WebDriverWait(webdriver, DEFAULT_WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, MODEL_CHOOSE_OLX_XPATH))
    )

    while current <= max_tries:
        car_list = webdriver.find_element(By.XPATH, MODEL_CHOOSE_OLX_XPATH)
        try:
            car_list.click()  # Expand the list of car models
        except StaleElementReferenceException:  # Element moved
            current += 1
            continue

        cars_to_choose = car_list.find_elements(By.CLASS_NAME, CAR_TO_CHOOSE_CLASS_OLX)
        model = car_model.capitalize()
        try:
            for car in cars_to_choose:
                try:
                    p_element = car.find_element(By.TAG_NAME, "p")
                    if p_element.text == model:
                        car.click()
                        break
                except NoSuchElementException:
                    continue
            break
        except StaleElementReferenceException:
            current += 1
            continue

    assert car_list is not None, "Car list should be present at this moment!"
    car_list.click()
