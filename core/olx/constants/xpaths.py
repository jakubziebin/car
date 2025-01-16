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
FROM_PRODUCTION_YEAR_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Rok prod.")]/following::input[@name="range-from-input"][1]'
)
TO_PRODUCTION_YEAR_OLX_XPATH: Final[str] = (
    '//div[contains(text(), "Rok prod.")]/following::input[@name="range-to-input"][1]'
)
