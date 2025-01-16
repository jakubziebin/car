from __future__ import annotations

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from car.core.olx.constants import CHROME_DRIVER_PATH, OLX_URL
from car.utils.olx.confirm_privacy_terms import confirm_olx_privacy_terms
from car.utils.olx.search_car import (
    paste_car_model_in_olx_search,
    confirm_search_olx,
    set_max_price_olx,
    choose_car_model_olx,
    set_category_olx,
    set_production_year_fork_olx,
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
    set_category_olx(driver)
    choose_car_model_olx(driver, "rio")
    set_production_year_fork_olx(driver, from_year=2014, to_year=2018)
    time.sleep(1000)
