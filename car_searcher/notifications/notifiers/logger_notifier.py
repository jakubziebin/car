from __future__ import annotations

from car_searcher.notifications.notifiers.abc.notifier import CarAd, Notifier


class LoggerNotifier(Notifier):
    def notify(self, ads: list[CarAd]) -> None:
        print(f"Found {len(ads)} new ads")  # TODO: change to the custom logger after creation

        for ad in ads:
            print(ad)
