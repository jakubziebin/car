from __future__ import annotations

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from car.car.core.constants import CHROME_DRIVER_PATH, OLX_URL
from car.car.utils.confirm_privacy_terms import confirm_olx_privacy_terms
from car.car.utils.search_car import (
    paste_car_model_in_olx_search,
    confirm_search_olx,
    set_max_price_olx,
    choose_car_model_olx,
)


def main():
    print("Hello from car!")


if __name__ == "__main__":
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(OLX_URL)
    confirm_olx_privacy_terms(driver)
    paste_car_model_in_olx_search(driver, "Kia", "rio")
    confirm_search_olx(driver)
    set_max_price_olx(driver, 40_000)
    choose_car_model_olx(driver, "rio")
    time.sleep(1000)
