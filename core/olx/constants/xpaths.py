from __future__ import annotations

from typing import Final

MODEL_CHOOSE_OLX_XPATH: Final[str] = (
    """//span[text()="Model"]/following::div[@data-testid="flyout-wrapper"][1]"""
)
CATEGORY_DROPDOWN_OLX_XPATH: Final[str] = '//div[@data-cy="category-dropdown"]'
ALL_CATEGORIES_OLX_XPATH: Final[str] = './/div[text()="Wszystkie kategorie"]'
MOTORIZATION_OLX_XPATH: Final[str] = '//li[.//span[text()="Motoryzacja"]]'
CAR_CATEGORY_OLX_XPATH: Final[str] = (
    '//li[contains(text(), "Samochody osobowe") or .//span[text()="Samochody osobowe"]]'
)
FUEL_TYPE_DROPDOWN_OLX_XPATH = (
    '//span[text()="Paliwo"]/following::div[@data-testid="flyout-wrapper"][1]'
)
DRIVE_TYPE_DROPDOWN_OLX_XPATH = (
    '//span[text()="Napęd"]/following::div[@data-testid="flyout-wrapper"][1]'
)
GEARBOX_TYPE_DROPDOWN_OLX_XPATH = (
    '//span[text()="Skrzynia biegów"]/following::div[@data-testid="flyout-wrapper"][1]'
)
BODY_TYPE_DROPDOWN_OLX_XPATH = (
    '//span[text()="Typ nadwozia"]/following::div[@data-testid="flyout-wrapper"][1]'
)
FROM_PRODUCTION_YEAR_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Rok prod.")]/following::input[@name="range-from-input"][1]'
)
TO_PRODUCTION_YEAR_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Rok prod.")]/following::input[@name="range-to-input"][1]'
)
FROM_ENGINE_CAPACITY_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Poj. silnika")]/following::input[@name="range-from-input"][1]'
)
TO_ENGINE_CAPACITY_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Poj. silnika")]/following::input[@name="range-to-input"][1]'
)
MIN_MILEAGE_INPUT_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Przebieg")]/following::input[@name="range-from-input"][1]'
)
MAX_MILEAGE_INPUT_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Przebieg")]/following::input[@name="range-to-input"][1]'
)
MIN_POWER_INPUT_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Moc silnika")]/following::input[@name="range-from-input"][1]'
)
MAX_POWER_INPUT_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Moc silnika")]/following::input[@name="range-to-input"][1]'
)
