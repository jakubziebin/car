from __future__ import annotations

from typing import Final

MODEL_CHOOSE_OLX_XPATH: Final[str] = (
    """//span[text()="Model"]/following::div[@data-testid="flyout-wrapper"][1]"""
)
