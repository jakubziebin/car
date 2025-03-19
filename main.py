from __future__ import annotations

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from car_searcher.core.olx.constants import OLX_URL
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
    chrome_options = Options()

    is_running_in_container = os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", False)
    if is_running_in_container:
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(OLX_URL)

    ranges_config = CarRangesConfig(
        max_price=60_000,
        min_year=2014,
        max_year=2020,
        min_capacity=900,
        max_mileage=100_000,
        min_power=80,
    )

    car_properties_config = OlxCarPropertiesConfig(
        fuel_types=["Benzyna"],
        drive_types=["Na przednie koła"],
        gearbox_types=["Manualna"],
        body_types=["Hatchback"],
        technical_conditions=["Nieuszkodzony"],
    )

    confirm_olx_privacy_terms(driver)

    CarSearcher(driver, "Kia", "rio").execute_car_search()
    OlxRangeInputsSetter(driver, ranges_config).execute_range_inputs_filling()
    OlxDropdownInputsSetter(driver, car_properties_config).execute_dropdown_inputs_set()
    OlxLocationSetter(driver, "katowice", "+100 km").execute_location_set()
    time.sleep(100000)
