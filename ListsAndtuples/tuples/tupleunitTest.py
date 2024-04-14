import unittest

# This class contains unit tests for tuple unpacking in Python.
class TupleUnpackingTests(unittest.TestCase):
    # This test checks if a tuple with three elements can be correctly unpacked into three variables.
    def test_unpacking_tuple_with_three_elements(self):
        # A tuple with three elements is created.
        data = (12, "apple", 3.14)
        # The tuple is unpacked into three variables.
        id, name, price = data
        # The values of the variables are checked to ensure they match the original tuple elements.
        self.assertEqual(id, 12)
        self.assertEqual(name, "apple")
        self.assertEqual(price, 3.14)

    # This test checks if a ValueError is raised when trying to unpack a tuple with three elements into two variables.
    def test_unpacking_tuple_with_incorrect_number_of_variables(self):
        # A tuple with three elements is created.
        data = (12, "apple", 3.14)
        # A ValueError is expected when trying to unpack the tuple into two variables.
        with self.assertRaises(ValueError):
            id, name = data

    # This test checks if a ValueError is raised when trying to unpack an empty tuple into three variables.
    def test_unpacking_empty_tuple(self):
        # An empty tuple is created.
        data = ()
        # A ValueError is expected when trying to unpack the empty tuple into three variables.
        with self.assertRaises(ValueError):
            id, name, price = data

# The unittest module's main function is called to run the tests when the script is run directly.
if __name__ == '__main__':
    unittest.main()