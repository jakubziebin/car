from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from car.car.core.constants import (
    SEARCH_INPUT_ID_OLX,
    CAR_TO_CHOOSE_CLASS_OLX,
    MAX_PRICE_INPUT_NAME_OLX,
    DEFAULT_WAIT_TIMEOUT,
    MODEL_CHOOSE_OLX_XPATH,
)
from car.car.core.constants.xpaths import (
    ALL_CATEGORIES_OLX_XPATH,
    CATEGORY_DROPDOWN_OLX_XPATH,
    MOTORIZATION_OLX_XPATH,
    CAR_CATEGORY_OLX_XPATH,
)

if TYPE_CHECKING:
    from selenium.webdriver import Chrome


def paste_car_model_in_olx_search(
    webdriver: Chrome, car_brand: str, car_model: str
) -> None:
    input_component = webdriver.find_element(By.ID, SEARCH_INPUT_ID_OLX)
    input_component.send_keys(f"{car_brand} {car_model}")


def confirm_search_olx(webdriver: Chrome) -> None:
    webdriver.find_element(By.ID, SEARCH_INPUT_ID_OLX).submit()


def set_max_price_olx(webdriver: Chrome, max_price: int) -> None:
    """Wait for max price input to be present and set the max price."""

    WebDriverWait(webdriver, DEFAULT_WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.NAME, MAX_PRICE_INPUT_NAME_OLX))
    )

    max_price_input = webdriver.find_element(By.NAME, MAX_PRICE_INPUT_NAME_OLX)
    max_price_input.send_keys(str(max_price))


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
    WebDriverWait(webdriver, DEFAULT_WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, MODEL_CHOOSE_OLX_XPATH))
    )
    car_list = webdriver.find_element(By.XPATH, MODEL_CHOOSE_OLX_XPATH)
    car_list.click()  # Expand the list of car models

    cars_to_choose = car_list.find_elements(By.CLASS_NAME, CAR_TO_CHOOSE_CLASS_OLX)
    car_model = car_model.capitalize()

    for car in cars_to_choose:
        try:
            p_element = car.find_element(By.TAG_NAME, "p")
            if p_element.text == car_model:
                car.click()
                break
        except NoSuchElementException:
            continue
