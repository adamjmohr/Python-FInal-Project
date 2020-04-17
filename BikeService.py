# Business layer program logic.
# Author: Adam Mohr

from DataStore import DataStore
from BikeRecord import BikeRecord


class BikeService:
    """A class used to represent the business logic and delegates actions to data layer."""

    def __init__(self):
        """Default Constructor to initialize data/persistence layer and fetch records from csv."""

        self.data_store = DataStore()
        self.list_records = self.data_store.get_all_records()

    def print_all(self):
        """Method to print all the records to console and every 9 records my name - Adam Mohr."""

        count = 0
        for row in self.list_records:
            print(row)
            count += 1
            if count % 9 == 0:
                self.print_adam()

        self.print_length()

    @staticmethod
    def get_input_new_record():
        """Helper method to get input from user."""

        year = input("Enter year: ")
        sex = input("Enter sex: ")
        age_group = input("Enter age group: ")
        student_response = input("Enter student response: ")
        vector = input("Enter vector: ")
        coordinate = input("Enter coordinate: ")
        value = input("Enter value: ")
        new_record = BikeRecord(year, "Canada", "", sex, age_group, student_response, "Percent", "239", "units", "0",
                                vector, coordinate, value, "", "", "", "0")

        return new_record

    def insert_bike_record(self):
        """Method to insert new Bike Record at end of the list. Hardcoded certain values and left some fields blank
        to match formatting found in original csv file."""

        self.list_records.append(self.get_input_new_record())
        print("Record added.")

    @staticmethod
    def print_adam():
        """Method to print the author's name - Adam Mohr."""

        print("Program by: Adam Mohr")

    def print_length(self):
        """Helper method to print length of list i.e. how many records."""

        print(len(self.list_records), "Records found")

    def save_records(self):
        """Method to save a new csv file to disk using DataStore method."""

        self.data_store.save_records_to_disk()

    def update_record(self):
        """Helper method to get valid list index number from user."""

        self.print_length()
        try:
            index = int(input("Enter index of record to update (starts at index 0): "))
            self.list_records[index] = self.get_input_new_record()
            print("Record index", index, "updated.")
        except IndexError as e:
            print(e, "please give valid index number (starts at index 0).")
        except ValueError as e:
            print(e, "please give valid integer number.")

    def show_record(self):
        """Method to show a single record."""

        self.print_length()
        try:
            index = int(input("Enter index of record to show (starts at index 0): "))
            print(self.list_records[index])
        except IndexError as e:
            print(e, "please give valid index number (starts at index 0).")
        except ValueError as e:
            print(e, "please give valid integer number.")

    def delete_record(self):
        """Method to delete a single record."""

        self.print_length()
        try:
            index = int(input("Enter index of record to delete (starts at index 0): "))
            self.list_records.pop(index)
            print("Record index", index, "deleted.")
        except IndexError as e:
            print(e, "please give valid index number (starts at index 0).")
        except ValueError as e:
            print(e, "please give valid integer number.")

    def sort_column(self):
        """Method to sort by column. Input is retrieved from user to determine which column to sort. Inline lambda
        function is used with a key that identifies the sorting property."""

        column = input("Enter column number to sort by: 0 = Sex, 1 = Age group, 2 = Student response, 3 = VECTOR, "
                       "4 = COORDINATE, "
                       " 5 = VALUE: ")
        if column == "0":
            self.list_records.sort(key=lambda x: x.sex)
        elif column == "1":
            self.list_records.sort(key=lambda x: x.age)
        elif column == "2":
            self.list_records.sort(key=lambda x: x.response)
        elif column == "3":
            self.list_records.sort(key=lambda x: x.vector)
        elif column == "4":
            self.list_records.sort(key=lambda x: x.coordinate)
        elif column == "5":
            self.list_records.sort(key=lambda x: int(x.value))
        else:
            print("Not a valid column number")

    @staticmethod
    def print_stars(num):
        """Static helper method to print out the number of stars to use in the histogram."""

        for i in range(num):
            print("*", end='')
        print()

    def print_chart(self, rarely, sometimes, often, always, dont):
        """Used with print_stars to create the formatted histogram and output it to console."""

        print("How often do you wear your bicycle helmet while cycling?")
        print("Rarely or never (", end='')
        print(rarely, ")       |", end='', sep='')
        self.print_stars(rarely)
        print("Sometimes (", end='')
        print(sometimes, ")             |", end='', sep='')
        self.print_stars(sometimes)
        print("Often (", end='')
        print(often, ")                 |", end='', sep='')
        self.print_stars(often)
        print("Always (", end='')
        print(always, ")                |", end='', sep='')
        self.print_stars(always)
        print("Do not ride a bicycle (", end='')
        print(dont, ") |", end='', sep='')
        self.print_stars(dont)

    def generate_histogram(self):
        """Retrieves input and generates histogram data based on user input. Loops through list of records and
        increments the specific count when the response condition is satisfied. Uses print_chart to output the data."""

        print("How you would like to visualize data chart?")
        print("a: age and gender, b: aggregate female, c: aggregate male, d: 11 years, e: 13 years, "
              "f: 15 years, g: all data")
        response = input("Please enter an option found above: ")
        response = response.lower()
        count_rarely = 0
        count_sometimes = 0
        count_often = 0
        count_always = 0
        count_dont = 0

        if response == "a":
            gender = input("Male or female? Enter m: male, f: female: ")
            gender = gender.lower()
            if gender == "m":
                gender = "Males"
            elif gender == "f":
                gender = "Females"
            else:
                print("Please enter a valid option. Back to main menu.")
                return
            age = input("Age range? Enter 11, 13, or 15: ")
            if age == "11":
                age = "11 years"
            elif age == "13":
                age = "13 years"
            elif age == "15":
                age = "15 years"
            else:
                print("Please enter a valid option. Back to main menu.")
                return
            for record in self.list_records:
                if record.sex == gender and record.age == age and record.response == "Rarely or never":
                    count_rarely += 1
                elif record.sex == gender and record.age == age and record.response == "Sometimes":
                    count_sometimes += 1
                elif record.sex == gender and record.age == age and record.response == "Often":
                    count_often += 1
                elif record.sex == gender and record.age == age and record.response == "Always":
                    count_always += 1
                elif record.sex == gender and record.age == age and record.response == "Do not ride a bicycle":
                    count_dont += 1
            print(gender, ", ", age, sep='')
            self.print_chart(count_rarely, count_sometimes, count_often, count_always, count_dont)
        elif response == "b":
            for record in self.list_records:
                if record.sex == "Females" and record.response == "Rarely or never":
                    count_rarely += 1
                elif record.sex == "Females" and record.response == "Sometimes":
                    count_sometimes += 1
                elif record.sex == "Females" and record.response == "Often":
                    count_often += 1
                elif record.sex == "Females" and record.response == "Always":
                    count_always += 1
                elif record.sex == "Females" and record.response == "Do not ride a bicycle":
                    count_dont += 1
            print("Females, all ages:")
            self.print_chart(count_rarely, count_sometimes, count_often, count_always, count_dont)
        elif response == "c":
            for record in self.list_records:
                if record.sex == "Males" and record.response == "Rarely or never":
                    count_rarely += 1
                elif record.sex == "Males" and record.response == "Sometimes":
                    count_sometimes += 1
                elif record.sex == "Males" and record.response == "Often":
                    count_often += 1
                elif record.sex == "Males" and record.response == "Always":
                    count_always += 1
                elif record.sex == "Males" and record.response == "Do not ride a bicycle":
                    count_dont += 1
            print("Males, all ages:")
            self.print_chart(count_rarely, count_sometimes, count_often, count_always, count_dont)
        elif response == "d":
            for record in self.list_records:
                if record.age == "11 years" and record.response == "Rarely or never":
                    count_rarely += 1
                elif record.age == "11 years" and record.response == "Sometimes":
                    count_sometimes += 1
                elif record.age == "11 years" and record.response == "Often":
                    count_often += 1
                elif record.age == "11 years" and record.response == "Always":
                    count_always += 1
                elif record.age == "11 years" and record.response == "Do not ride a bicycle":
                    count_dont += 1
            print("11 years old:")
            self.print_chart(count_rarely, count_sometimes, count_often, count_always, count_dont)
        elif response == "e":
            for record in self.list_records:
                if record.age == "13 years" and record.response == "Rarely or never":
                    count_rarely += 1
                elif record.age == "13 years" and record.response == "Sometimes":
                    count_sometimes += 1
                elif record.age == "13 years" and record.response == "Often":
                    count_often += 1
                elif record.age == "13 years" and record.response == "Always":
                    count_always += 1
                elif record.age == "13 years" and record.response == "Do not ride a bicycle":
                    count_dont += 1
            print("13 years old:")
            self.print_chart(count_rarely, count_sometimes, count_often, count_always, count_dont)
        elif response == "f":
            for record in self.list_records:
                if record.age == "15 years" and record.response == "Rarely or never":
                    count_rarely += 1
                elif record.age == "15 years" and record.response == "Sometimes":
                    count_sometimes += 1
                elif record.age == "15 years" and record.response == "Often":
                    count_often += 1
                elif record.age == "15 years" and record.response == "Always":
                    count_always += 1
                elif record.age == "15 years" and record.response == "Do not ride a bicycle":
                    count_dont += 1
            print("15 years old:")
            self.print_chart(count_rarely, count_sometimes, count_often, count_always, count_dont)
        elif response == "g":
            for record in self.list_records:
                if record.response == "Rarely or never":
                    count_rarely += 1
                elif record.response == "Sometimes":
                    count_sometimes += 1
                elif record.response == "Often":
                    count_often += 1
                elif record.response == "Always":
                    count_always += 1
                elif record.response == "Do not ride a bicycle":
                    count_dont += 1
            print("Males, Females, All ages:")
            self.print_chart(count_rarely, count_sometimes, count_often, count_always, count_dont)
        else:
            print("Please enter a valid option. Back to main menu.")
