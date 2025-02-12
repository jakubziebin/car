from __future__ import annotations

from typing import Callable, ClassVar, TypeAlias

from selenium.common.exceptions import StaleElementReferenceException

from car.exceptions.car_exception import CarException


class StaleElementMaxTriesExceedError(CarException):
    """Raises when tried to find stale element more than `max_tries` times."""


CallableToPreventStaleElement: TypeAlias = Callable[..., bool]


class StaleElementHandler:
    MAX_TRIES: ClassVar[int] = 3  # override to modify

    def __init__(
        self, executable: CallableToPreventStaleElement, *args, **kwargs
    ) -> None:
        """
        Initialize StaleElementHandler.

        Args:
            executable: function to execute in the handler. Must return bool either passed or not.
        """
        self._executable = executable
        self._args = args
        self._kwargs = kwargs

    def execute(self) -> None:
        """Tries to execute `element_click_function` `max_tries` times."""
        current = 0
        exception: StaleElementReferenceException | None = None

        while current <= self.MAX_TRIES:
            try:
                result = self._executable(*self._args, **self._kwargs)
                if result:
                    return
            except StaleElementReferenceException as error:
                current += 1
                exception = error
                continue

        raise StaleElementMaxTriesExceedError from exception

    def switch_executable(self, new_executable: CallableToPreventStaleElement) -> None:
        """Switches function to execute"""
        self._executable = new_executable
