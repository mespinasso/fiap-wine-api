from typing import List


class YearlyWineGrapeData:
    def __init__(self, year: int, amount: int):
        self.year = year
        self.amount = amount

    def to_dict(self):
        return {'year': self.year, 'amount': self.amount}


class WineGrape:
    def __init__(self, code: str, name: str, category: str):
        self.code = code
        self.name = name
        self.category = category
        self.data: List[YearlyWineGrapeData] = []

    def add_yearly_data(self, yearly_data: YearlyWineGrapeData):
        self.data.append(yearly_data)

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'category': self.category,
            'data': [yearly_data.to_dict() for yearly_data in self.data]
        }
