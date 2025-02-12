from __future__ import annotations

from typing import TypeAlias

XPath: TypeAlias = str


def get_location_choose_xpath(city: str) -> XPath:
    return f"//form[@data-testid='listing-filters-form']//li[@data-cy='suggestion-item']//div[contains(text(), '{city.capitalize()}')]"
