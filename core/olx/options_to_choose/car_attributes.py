from __future__ import annotations

from typing import Literal

CarPossibleFuelOlx = Literal[
    "Wszystkie",
    "Benzyna",
    "Diesel",
    "LPG",
    "CNG i Hybryda",
    "Hybryda Plug-in",
    "Elektryczny",
]
CarPossibleDriveOlx = Literal[
    "Wszystkie",
    "4X4 (dołączany automatycznie)",
    "4X4 (dołączany ręcznie)",
    "Na przednie koła",
    "Na tylne koła",
]
CarPossibleGearboxOlx = Literal["Wszystkie", "Manualna", "Automatyczna"]
CarPossibleBodyOlx = Literal[
    "Wszystie",
    "Kabriolet",
    "Sedan",
    "Coupe",
    "Pickup",
    "Hatchback",
    "Kombi",
    "Terenowy",
    "Minibus",
    "Minivan",
    "SUV",
]
CarPossibleCountryProductionOlx = Literal[
    "Wszystkie",
    "Polska",
    "Austria",
    "Czechy",
    "Finlandia",
    "Hiszpania",
    "Holandia",
    "Kanada",
    "Niemcy",
    "Słowacja",
    "Stany Zjednoczone",
    "Szwajcaria",
    "Szwecja",
    "Włochy",
    "Wielka Brytania",
]
CarPossibleColorOlx = Literal[
    "Wszystkie",
    "Biały",
    "Czarny",
    "Szary",
    "Srebrny",
    "Niebieski",
    "Brązowy - Beżowy",
    "Czerwony",
    "Zielony",
    "Żółty - Złoty",
    "Inny kolor",
]
CarSteeringWheelPlacementOlx = Literal["Wszystkie", "po lewej", "po prawej"]
