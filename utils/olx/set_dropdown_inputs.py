from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Final, Any

from car.core.olx.constants import (
    DRIVE_TYPE_DROPDOWN_OLX_XPATH,
    GEARBOX_TYPE_DROPDOWN_OLX_XPATH,
    BODY_TYPE_DROPDOWN_OLX_XPATH,
    PRODUCTION_COUNTRY_DROPDOWN_OLX_XPATH,
    CAR_COLOR_DROPDOWN_OLX_XPATH,
    CAR_STEERING_WHEEL_PLACEMENT_DROPDOWN_OLX_XPATH,
    CAR_TECHNICAL_CONDITION_DROPDOWN_OLX_XPATH,
    FUEL_TYPE_DROPDOWN_OLX_XPATH,
)
from car.core.car_search_config.car_properties_config import BaseCarPropertiesConfig
from car.core.olx.options_to_choose.car_attributes import (
    CarPossibleFuelOlx,
    CarPossibleDriveOlx,
    CarPossibleGearboxOlx,
    CarPossibleBodyOlx,
    CarPossibleCountryProductionOlx,
    CarPossibleColorOlx,
    CarSteeringWheelPlacementOlx,
    CarTechnicalConditionOlx,
)
from car.utils.abc.dropdown_inputs_setter import BaseDropdownInputsSetter

if TYPE_CHECKING:
    from selenium.webdriver import Chrome


DEFAULT_CAR_PROPERTY_OLX: Final[str] = "Wszystkie"


def _get_default_property_olx_config() -> (
    list[Any]
):  # TODO: proper resolution of return type
    return [DEFAULT_CAR_PROPERTY_OLX]


@dataclass
class OlxCarPropertiesConfig(BaseCarPropertiesConfig):
    fuel_types: list[CarPossibleFuelOlx] = field(
        default_factory=_get_default_property_olx_config
    )
    drive_types: list[CarPossibleDriveOlx] = field(
        default_factory=_get_default_property_olx_config
    )
    gearbox_types: list[CarPossibleGearboxOlx] = field(
        default_factory=_get_default_property_olx_config
    )
    body_types: list[CarPossibleBodyOlx] = field(
        default_factory=_get_default_property_olx_config
    )
    production_countries: list[CarPossibleCountryProductionOlx] = field(
        default_factory=_get_default_property_olx_config
    )
    colors: list[CarPossibleColorOlx] = field(
        default_factory=_get_default_property_olx_config
    )
    steering_wheel_placements: list[CarSteeringWheelPlacementOlx] = field(
        default_factory=_get_default_property_olx_config
    )
    technical_conditions: list[CarTechnicalConditionOlx] = field(
        default_factory=_get_default_property_olx_config
    )


class OlxDropdownInputsSetter(BaseDropdownInputsSetter):
    def __init__(self, webdriver: Chrome, config: OlxCarPropertiesConfig) -> None:
        super().__init__(webdriver=webdriver, car_properties_config=config)

    @property
    def config(self) -> OlxCarPropertiesConfig:
        return self._config  # type: ignore[override, return-value]

    def execute_dropdown_inputs_set(self) -> None:
        self.set_fuel_type()
        self.set_drive_type()
        self.set_gearbox_type()
        self.set_body_type()
        self.set_country_production()
        self.set_car_colors()
        self.set_country_production()
        self.set_car_technical_condition()

    def set_fuel_type(self) -> None:
        """Set fuel type in the dropdown on the OLX webste."""
        self.set_dropdown_options(FUEL_TYPE_DROPDOWN_OLX_XPATH, *self.config.fuel_types)

    def set_drive_type(self) -> None:
        """Set drive type in the dropdown on the OLX website."""
        self.set_dropdown_options(
            DRIVE_TYPE_DROPDOWN_OLX_XPATH, *self.config.drive_types
        )

    def set_gearbox_type(self) -> None:
        """Set gearbox type in the dropdown on the OLX website."""
        self.set_dropdown_options(
            GEARBOX_TYPE_DROPDOWN_OLX_XPATH, *self.config.gearbox_types
        )

    def set_body_type(self) -> None:
        """Set body type in the dropdown on the OLX website."""
        self.set_dropdown_options(BODY_TYPE_DROPDOWN_OLX_XPATH, *self.config.body_types)

    def set_country_production(self) -> None:
        """Set country production in the dropdown on the OLX website."""
        self.set_dropdown_options(
            PRODUCTION_COUNTRY_DROPDOWN_OLX_XPATH, *self.config.production_countries
        )

    def set_car_colors(self) -> None:
        """Set car colors in the dropdown on the OLX website."""
        self.set_dropdown_options(CAR_COLOR_DROPDOWN_OLX_XPATH, *self.config.colors)

    def set_car_steering_wheel_placement(self) -> None:
        """Set car steering wheel placement in the dropdown on the OLX website."""
        self.set_dropdown_options(
            CAR_STEERING_WHEEL_PLACEMENT_DROPDOWN_OLX_XPATH,
            *self.config.steering_wheel_placements,
        )

    def set_car_technical_condition(self) -> None:
        """Set car technical condition in the dropdown on the OLX website."""
        self.set_dropdown_options(
            CAR_TECHNICAL_CONDITION_DROPDOWN_OLX_XPATH,
            *self.config.technical_conditions,
        )
