# Represents a bike helmet record from a csv file. All the instance attributes are from the columns in csv file.
# Author: Adam Mohr
from Record import Record


class BikeRecord(Record):
    """A subclass, inherits from Record, used to represent one row of a Bike Record data in a csv file."""

    """Class attribute to specify type of record."""
    record_type = __name__

    def __init__(self, year, country, dguid, sex, age, response, uom, uom_id, scalar_factor, scalar_id, vector,
                 coordinate, value, status, symbol, terminated, decimals):
        """Super constructor. Create object and initialize with instance attributes using Parent class Record's init."""
        super().__init__(year, country, dguid, sex, age, response, uom, uom_id, scalar_factor, scalar_id, vector,
                         coordinate, value, status, symbol, terminated, decimals)

    def __str__(self):
        """Print this object's properties and values specially formatted differently than parent class.
        Overrides method from Parent class Record."""
        return 'Year: ' + self.year + ', ' + 'Country: ' + self.country + ', ' + 'DGUID: ' + self.dguid + ', ' + \
            'Sex: ' + self.sex + ', ' + 'Age: ' + self.age + ', ' + 'Response: ' + self.response + ', ' + 'UoM: ' + \
            self.uom + ', ' + 'UoM ID: ' + self.uom_id + ', ' + 'Scalar Factor: ' + self.scalar_factor + ', ' + \
            'Scalar ID: ' + self.scalar_id + ', ' + 'Vector: ' + self.vector + ', ' + 'Coordinate: ' + \
            self.coordinate + ', ' + 'Value: ' + self.value + ', ' + 'Status: ' + self.status + ', ' + 'Symbol: ' + \
            self.symbol + ', ' + 'Terminated: ' + self.terminated + ', ' + 'Decimals: ' + self.decimals
