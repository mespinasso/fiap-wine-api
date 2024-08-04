from typing import List


class YearlyCountryData:
    def __init__(self, year: int, amount: int, value: int):
        self.year = year
        self.amount = amount
        self.value = value

    def to_dict(self):
        return {'year': self.year, 'amount': self.amount, 'value': self.value}


class Country:
    def __init__(self, name: str):
        self.name = name
        self.data: List[YearlyCountryData] = []

    def add_yearly_data(self, yearly_data: YearlyCountryData):
        self.data.append(yearly_data)

    def to_dict(self):
        return {
            'name': self.name,
            'data': [yearly_data.to_dict() for yearly_data in self.data]
        }
