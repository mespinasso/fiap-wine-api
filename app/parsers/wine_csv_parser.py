import csv
from typing import List

from app.models.wine_model import Wine, YearlyWineData


def parse_wine_data(csv_file: str, starting_year: int, ending_year: int) -> List[Wine]:
    wine_items = []

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            control = row['control']

            if '_' not in control:
                continue

            product = row['produto']
            category = control.split('_')[0] if '_' in control else control

            wine_item = Wine(code=control, name=product, category=category)

            for year in range(starting_year, ending_year):
                amount = int(row[str(year)])
                wine_item.add_yearly_data(YearlyWineData(year=year, amount=amount))

            wine_items.append(wine_item)

    return wine_items
