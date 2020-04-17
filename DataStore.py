# Data persistence layer of application.
# Author: Adam Mohr

import csv
from BikeRecord import BikeRecord


class DataStore:
    """A class used to store Bike Records in a simple list structure from csv file."""

    """Class variables for data set file names. If changing file names then change here."""
    file_name = "canadianBikeHelmet.csv"
    new_file_name = "newCanadianBikeHelmet.csv"

    def __init__(self):
        """Default Constructor to initialize an empty list and database connection."""

        self.list_records = []

    def load_records_from_csv(self):
        """Open csv file and read all rows using dict to store column headers as keys with each field's value.
         Then store as a Bike Record in the list."""

        try:
            with open(self.file_name, 'r', newline='', encoding='utf-8-sig') as csv_file:
                print("Opening file:", self.file_name)
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    # Create BikeRecords and add to list using key value pairs from column header names
                    self.list_records.append(
                        BikeRecord(row['REF_DATE'], row['GEO'], row['DGUID'], row['Sex'], row['Age group'],
                                   row['Student response'],
                                   row['UOM'], row['UOM_ID'], row['SCALAR_FACTOR'], row['SCALAR_ID'],
                                   row['VECTOR'],
                                   row['COORDINATE'], row['VALUE'],
                                   row['STATUS'], row['SYMBOL'], row['TERMINATED'], row['DECIMALS']))

                return self.list_records

        # Handle Exceptions and flag error to user. Exit program.
        except FileNotFoundError as e:
            print("File not found error:", e)
            exit()
        except csv.Error as e:
            print("Csv file error:", e)
            exit()

    def save_records_to_disk(self):
        """Method to save a new csv file of records to disk."""

        with open(self.new_file_name, 'w', newline='', encoding='utf-8-sig') as csv_file:
            print("Writing to file:", self.new_file_name)
            writer = csv.writer(csv_file)
            writer.writerow(
                ['REF_DATE', 'GEO', 'DGUID', 'Sex', 'Age group', 'Student response', 'UOM', 'UOM_ID', 'SCALAR_FACTOR',
                 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'])

            for record in self.list_records:
                writer.writerow(
                    [record.year, record.country, record.dguid, record.sex, record.age, record.response, record.uom,
                     record.uom_id, record.scalar_factor,
                     record.scalar_id, record.vector, record.coordinate, record.value, record.status, record.symbol,
                     record.terminated, record.decimals])

    def get_all_records(self):
        """Method to reload records from disk and start from original data set."""

        return self.load_records_from_csv()
