from __future__ import annotations

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from car.core.olx.constants import CHROME_DRIVER_PATH, OLX_URL
from car.utils.olx.confirm_privacy_terms import confirm_olx_privacy_terms
from car.utils.olx.search_car import CarSearcher
from car.utils.olx.set_dropdown_inputs import (
    set_fuel_type_olx,
    set_drive_type_olx,
    set_gearbox_type_olx,
    set_body_type_olx,
    set_country_production_olx,
    set_car_colors_olx,
    set_car_steering_wheel_placement_olx,
    set_car_technical_condition_olx,
)
from car.utils.olx.set_search_ranges import OlxRangeInputsSetter
from car.core.car_search_config.range_config import CarRangesConfig


if __name__ == "__main__":
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(OLX_URL)

    ranges_config = CarRangesConfig(
        max_price=40_000,
        min_year=2014,
        max_year=2020,
        min_capacity=1250,
        max_mileage=100_000,
        min_power=85,
    )

    confirm_olx_privacy_terms(driver)

    CarSearcher(driver, "Kia", "rio").execute_car_search()
    OlxRangeInputsSetter(driver, ranges_config).execute_range_inputs_filling()

    set_fuel_type_olx(driver, "Benzyna")
    set_drive_type_olx(driver, "Na przednie koła")
    set_gearbox_type_olx(driver, "Manualna")
    set_body_type_olx(driver, "Hatchback")
    set_country_production_olx(driver, "Polska", "Niemcy")
    set_car_colors_olx(driver, "Biały", "Czarny", "Szary", "Czerwony")
    set_car_steering_wheel_placement_olx(driver, "po prawej")
    set_car_technical_condition_olx(driver, "Nieuszkodzony")
    time.sleep(1000)
