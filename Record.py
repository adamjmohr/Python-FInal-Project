# Represents a generic record from a csv file. All the instance attributes are from the columns in csv file.
# Author: Adam Mohr


class Record:
    """A class used to represent one row of a generic data record in a csv file. Subclasses will inherit from this
    parent class."""

    """Class attribute to specify type of record."""
    record_type = __name__

    def __init__(self, year, country, dguid, sex, age, response, uom, uom_id, scalar_factor,
                 scalar_id, vector, coordinate, value, status, symbol, terminated, decimals):
        """Create object and initialize with Instance attributes."""
        self.year = year
        self.country = country
        self.dguid = dguid
        self.sex = sex
        self.age = age
        self.response = response
        self.uom = uom
        self.uom_id = uom_id
        self.scalar_factor = scalar_factor
        self.scalar_id = scalar_id
        self.vector = vector
        self.coordinate = coordinate
        self.value = value
        self.status = status
        self.symbol = symbol
        self.terminated = terminated
        self.decimals = decimals

    def __str__(self):
        """Print this object's attributes formatted with commas"""
        return self.year + ', ' + self.country + ', ' + self.dguid + ', ' + self.sex + ', ' + self.age \
            + ', ' + self.response + ', ' + self.uom + ', ' + self.uom_id + ', ' + self.scalar_factor \
            + ', ' + self.scalar_id + ', ' + self.vector + ', ' + self.coordinate + ', ' + self.value \
            + ', ' + self.status + ', ' + self.symbol + ', ' + self.terminated + ', ' + self.decimals
