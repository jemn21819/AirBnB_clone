#!/usr/bin/python3
"""
Test for the Place class
"""


from datetime import datetime
import inspect
from models import place
from models.base_model import BaseModel
import pep8
import unittest
Place = place.Place

c = "created_at"
u = "updated_at"


class TestStateDocStyle(unittest.TestCase):
    """test for documentation and pep8 style"""
    def setUp(cls):
        """set up for methods"""
        cls.place_func = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8(self):
        """test pep8 in Place class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_pep8_test(self):
        """test pep8 for test to Place class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_module_doc(self):
        """test for the doc in module"""
        self.assertIsNot(place.__doc__, None,
                         "place.py without a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py without a docstring")

    def test_class_doc(self):
        """test for class documentation"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class without docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class without docstring")

    def test_func_doc(self):
        """test for doc in methods"""
        for func in self.place_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} docstring needed in method".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} docstring needed in method".format(func[0]))


class TestPlaceClass(unittest.TestCase):
    """test for class"""
    def test_is_subclass(self):
        """test for a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id(self):
        """thest for for attribute city_id for Place class"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id(self):
        """test for the user_id attr"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name(self):
        """test for the name attribute in the Place class"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description(self):
        """test for description in Place class"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms(self):
        """test for number of rooms in Place class"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Place has attr number_bathrooms, and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_to_dict_values(self):
        """test the values in dict"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        new_dict = place.to_dict()
        self.assertEqual(new_dict["__class__"], "Place")
        self.assertEqual(type(new_dict[c]), str)
        self.assertEqual(type(new_dict[u]), str)
        self.assertEqual(new_dict[c], place.created_at.strftime(time))
        self.assertEqual(new_dict[u], place.updated_at.strftime(time))

    def test_max_guest_attr(self):
        """Test Place has attr max_guest, and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):
        """Test Place has attr price_by_night, and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Place has attr latitude, and it's a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        """Test Place has attr longitude, and it's a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_str(self):
        """test for output str method"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
