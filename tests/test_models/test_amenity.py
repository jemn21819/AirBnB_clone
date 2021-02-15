#!/usr/bin/python3
"""
Test for the Amenity class
"""


from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenity = amenity.Amenity

c = "created_at"
u = "updated_at"


class TestStateDocStyle(unittest.TestCase):
    """test for documentation and pep8 style"""
    def setUp(cls):
        """set up for methods"""
        cls.amenity_func = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8(self):
        """test pep8 in Amenity class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_pep8_test(self):
        """test pep8 for test to Amenity class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_module_doc(self):
        """test for the doc in module"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py without a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py without a docstring")

    def test_class_doc(self):
        """test for class documentation"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class without docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class without docstring")

    def test_func_doc(self):
        """test for doc in methods"""
        for func in self.amenity_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} docstring needed in method".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} docstring needed in method".format(func[0]))


class TestAmenityClass(unittest.TestCase):
    """test for class"""
    def test_is_subclass(self):
        """test for a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name(self):
        """test for the state_id attr"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict_values(self):
        """test the values in dict"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict[c]), str)
        self.assertEqual(type(new_dict[u]), str)
        self.assertEqual(new_dict[c], amenity.created_at.strftime(time))
        self.assertEqual(new_dict[u], amenity.updated_at.strftime(time))

    def test_str(self):
        """test for output str method"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
