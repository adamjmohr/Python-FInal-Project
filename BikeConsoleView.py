# Console based view layer to process user interaction.
# Author: Adam Mohr

from BikeService import BikeService


class BikeConsoleView:
    """A class used to represent the view layer that users can interact with."""

    def __init__(self):
        """Default Constructor to initialize business layer service."""

        self.service = BikeService()

    def show_menu(self):
        """Show the menu options to the user and retrieve input."""

        while True:
            self.print_menu()
            response = input("Enter an option: ")
            self.process_response(response)

    def print_menu(self):
        """Print the menu options to the user console."""

        self.service.print_adam()
        print("Please enter an option found below: ")
        print("a: show all bike records, v: show one record, i: insert new record, u: update record, d: delete record,")
        print("r: reload the dataset, w: write records to new csv file, s: sort the list of Records by column, "
              "h: show bar chart histogram, x: exit program")

    def process_response(self, entry):
        """Decision structure to get user input. Converts string input to lowercase."""

        entry = entry.lower()
        if entry == "a":
            self.print_list()
        elif entry == "r":
            print("Reloading dataset.")
            self.service = BikeService()
        elif entry == "w":
            self.service.save_records()
        elif entry == "v":
            self.service.show_record()
        elif entry == "i":
            self.service.insert_bike_record()
        elif entry == "u":
            self.service.update_record()
        elif entry == "d":
            self.service.delete_record()
        elif entry == "s":
            self.service.sort_column()
        elif entry == "h":
            self.service.generate_histogram()
        elif entry == "x":
            print("Exiting program.")
            self.service.print_adam()
            exit()
        else:
            print("Please enter a valid menu option.")

    def print_list(self):
        self.service.print_all()
