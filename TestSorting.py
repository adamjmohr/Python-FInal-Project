# Single unit test for sorting of records in application.
# Author: Adam Mohr

import unittest
from BikeService import BikeService
from BikeRecord import BikeRecord


class AdamTestCase(unittest.TestCase):
    """A test class to see if sorting of records' attributes works as intended."""

    def test_list_sort(self):
        """Creates a list of pre sorted values and compares to a test list of values in default position. They are
        not equal at this point. Then the test list is sorted and compared and now they should be equal."""
        sorted_values = [3, 4, 5, 7, 9, 10, 10, 10, 10, 11, 11, 11, 12, 13, 14, 15, 16, 16, 17, 17, 18, 21, 24, 31, 38,
                         41, 45, 47, 52, 63
                         ]
        self.service = BikeService()
        test_sorted_values = []
        for row in self.service.list_records:
            test_sorted_values.append(int(row.value))
        
        self.assertNotEqual(test_sorted_values, sorted_values)
        print(test_sorted_values)

        test_sorted_values.clear()
        self.service.sort_column()

        row: BikeRecord
        for row in self.service.list_records:
            test_sorted_values.append(int(row.value))

        self.assertEqual(test_sorted_values, sorted_values)
        print()
        print(sorted_values)
        print(test_sorted_values)
        print("Adam Mohr")


if __name__ == '__main__':
    unittest.main()
