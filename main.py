from __future__ import annotations

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from car_searcher.core.olx.constants import CHROME_DRIVER_PATH, OLX_URL
from car_searcher.utils.olx.confirm_privacy_terms import confirm_olx_privacy_terms
from car_searcher.utils.olx.search_car import CarSearcher
from car_searcher.utils.olx.set_dropdown_inputs import (
    OlxCarPropertiesConfig,
    OlxDropdownInputsSetter,
)
from car_searcher.utils.olx.set_location import OlxLocationSetter
from car_searcher.core.car_search_config.range_config import CarRangesConfig
from car_searcher.utils.olx.set_search_ranges import OlxRangeInputsSetter

if __name__ == "__main__":
    service = Service(CHROME_DRIVER_PATH)
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

    car_properties_config = OlxCarPropertiesConfig(
        fuel_types=["Benzyna"],
        drive_types=["Na przednie koła"],
        gearbox_types=["Manualna"],
        body_types=["Hatchback"],
        production_countries=["Polska", "Niemcy"],
        colors=["Biały", "Czarny", "Szary", "Czerwony"],
        steering_wheel_placements=["po prawej"],
        technical_conditions=["Nieuszkodzony"],
    )

    confirm_olx_privacy_terms(driver)

    CarSearcher(driver, "Kia", "rio").execute_car_search()
    OlxRangeInputsSetter(driver, ranges_config).execute_range_inputs_filling()
    OlxDropdownInputsSetter(driver, car_properties_config).execute_dropdown_inputs_set()
    OlxLocationSetter(driver, "katowice", "+100 km").execute_location_set()

    time.sleep(1000)
