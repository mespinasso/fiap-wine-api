import csv
from typing import List

from app.models.wine_model import WineGrape, YearlyWineGrapeData
from app.utils.validation_helpers import represents_int


def parse_data(csv_file: str, starting_year: int, ending_year: int, name_column: str, delimiter=';') -> List[WineGrape]:
    items = []

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            control = row['control']

            if '_' not in control:
                continue

            name = row[name_column]
            category = control.split('_')[0] if '_' in control else control

            wine_item = WineGrape(code=control, name=name, category=category)

            for year in range(starting_year, ending_year):
                raw_amount = row[str(year)]
                amount = 0

                if represents_int(raw_amount):
                    amount = int(raw_amount)

                wine_item.add_yearly_data(YearlyWineGrapeData(year=year, amount=amount))

            items.append(wine_item)

    return items
