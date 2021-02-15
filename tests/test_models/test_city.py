#!/usr/bin/python3
"""
Test for the City class
"""


from datetime import datetime
import inspect
from models import city
from models.base_model import BaseModel
import pep8
import unittest
City = city.City

c = "created_at"
u = "updated_at"


class TestStateDocStyle(unittest.TestCase):
    """test for documentation and pep8 style"""
    def setUp(cls):
        """set up for methods"""
        cls.city_func = inspect.getmembers(City, inspect.isfunction)

    def test_pep8(self):
        """test pep8 in City class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_pep8_test(self):
        """test pep8 for test to City class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_module_doc(self):
        """test for the doc in module"""
        self.assertIsNot(city.__doc__, None,
                         "city.py without a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py without a docstring")

    def test_class_doc(self):
        """test for class documentation"""
        self.assertIsNot(City.__doc__, None,
                         "City class without docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class without docstring")

    def test_func_doc(self):
        """test for doc in methods"""
        for func in self.city_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} docstring needed in method".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} docstring needed in method".format(func[0]))


class TestCityClass(unittest.TestCase):
    """test for class"""
    def test_is_subclass(self):
        """test for a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_state_id(self):
        """thest for for attribute state id for City class"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_name(self):
        """test for the state_id attr"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_to_dict_values(self):
        """test the values in dict"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict[c]), str)
        self.assertEqual(type(new_dict[u]), str)
        self.assertEqual(new_dict[c], city.created_at.strftime(time))
        self.assertEqual(new_dict[u], city.updated_at.strftime(time))

    def test_str(self):
        """test for output str method"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
