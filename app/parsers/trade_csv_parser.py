import csv
from itertools import count
from typing import List

from app.models.country_model import Country, YearlyCountryData
from app.utils.validation_helpers import represents_int


def parse_data(csv_file: str, starting_year: int, ending_year: int, name_column='País', delimiter=';') -> List[Country]:
    items = []

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        fieldnames = remap(next(reader))

        print(fieldnames)

        for row in reader:
            row = dict(zip(fieldnames, row))

            country = Country(name=row[name_column])

            for year in range(starting_year, ending_year):
                raw_amount = row[f'{str(year)}_amount']
                amount = 0

                raw_value = row[f'{str(year)}_value']
                value = 0

                if represents_int(raw_amount):
                    amount = int(raw_amount)

                if represents_int(raw_value):
                    value = int(raw_value)

                country.add_yearly_data(YearlyCountryData(year=year, amount=amount, value=value))

            items.append(country)

    return items


def remap(field_names):
    changed_field_names = []
    last_field = ''

    for field in field_names:
        if represents_int(field):
            if last_field != '' and last_field.startswith(field):
                field = f'{field}_value'
            else:
                field = f'{field}_amount'

            last_field = field

        changed_field_names.append(field)

    return changed_field_names
