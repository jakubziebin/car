from __future__ import annotations

import os
import json
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

from car_searcher.ad_trackers.car_ad import CarAd


class OlxAdTracker:
    def __init__(
        self, driver: webdriver.Chrome, storage_file: str = "car_ads_history.json"
    ) -> None:
        self.driver = driver
        self.storage_file = storage_file
        self.known_ads: dict[str, CarAd] = self.load_known_ads()

    def load_known_ads(self) -> dict[str, CarAd]:
        if not os.path.exists(self.storage_file):
            return {}

        with open(self.storage_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {
                ad_id: CarAd(
                    id=ad_data["id"],
                    title=ad_data["title"],
                    price=ad_data["price"],
                    url=ad_data["url"],
                    location=ad_data["location"],
                    date_found=datetime.fromisoformat(ad_data["date_found"]),
                )
                for ad_id, ad_data in data.items()
            }

    def save_known_ads(self) -> None:
        data = {
            ad.id: {
                "title": ad.title,
                "price": ad.price,
                "url": ad.url,
                "location": ad.location,
                "date_found": ad.date_found.isoformat(),
            }
            for ad_id, ad in self.known_ads.items()
        }

        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_current_ads(self) -> list[CarAd]:
        ads = self.driver.find_elements(By.CSS_SELECTOR, "[data-cy='l-card']")

        current_ads = []
        for ad in ads:
            try:
                ad_id = ad.get_attribute("id")
                title = ad.find_element(By.CSS_SELECTOR, "[data-cy='l-card'] h6").text
                price = float(
                    ad.find_element(By.CSS_SELECTOR, "[data-testid='ad-price']")
                    .text.replace(" ", "")
                    .replace("zł", "")
                    .replace(",", ".")
                )
                url = ad.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                location = (
                    ad.find_element(By.CSS_SELECTOR, "[data-testid='location-date']")
                    .text.split("-")[0]
                    .strip()
                )

                current_ads.append(
                    CarAd(
                        id=ad_id,
                        title=title,
                        price=price,
                        url=url,
                        location=location,
                        date_found=datetime.now(),
                    )
                )
            except Exception as e:
                print(f"Błąd podczas przetwarzania ogłoszenia: {e}")
                continue

        return current_ads
