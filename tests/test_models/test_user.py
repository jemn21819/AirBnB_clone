#!/usr/bin/python3
"""
Test for the User class
"""


from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User

c = "created_at"
u = "updated_at"


class TestUserDocStyle(unittest.TestCase):
    """test for documentation and pep8 style"""
    def setUp(cls):
        """set up for methods"""
        cls.user_func = inspect.getmembers(User, inspect.isfunction)

    def test_pep8(self):
        """test pep8 in User Class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_pep8_test(self):
        """test pep8 for test to User class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_module_doc(self):
        """test for the doc in module"""
        self.assertIsNot(user.__doc__, None,
                         "User.py without a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "User.py without a docstring")

    def test_class_doc(self):
        """test for class documentation"""
        self.assertIsNot(User.__doc__, None,
                         "User class without docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class without docstring")

    def test_func_doc(self):
        """test for doc in methods"""
        for func in self.user_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} docstring needed in method".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} docstring needed in method".format(func[0]))


class TestUserClass(unittest.TestCase):
    """test for class"""
    def test_is_subclass(self):
        """test for a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email(self):
        """test for email attribute"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """test for password attribute"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        """test for the first name attribute"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """test for last name attribute and if is string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_to_dict_creat(self):
        """test to_dict method create dictionary with correct att"""
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in user.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test the values in dict"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict[c]), str)
        self.assertEqual(type(new_dict[u]), str)
        self.assertEqual(new_dict[c], user.created_at.strftime(time))
        self.assertEqual(new_dict[u], user.updated_at.strftime(time))

    def test_str(self):
        """test for output str method"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
