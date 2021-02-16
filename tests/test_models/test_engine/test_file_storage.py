#!/usr/bin/python3
"""
Module thats contain test for file storage
"""
import os
import json
import pep8
import inspect
import unittest
from models.user import User
from models.city import City
from datetime import datetime
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.engine import file_storage
from models.base_model import BaseModel
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDoc(unittest.TestCase):
    """Testing documentation and style FileStorage class"""

    def setUp(cls):
        """set up for methods testing"""
        cls.fs_func = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8(self):
        """test pep8 in FileStorage class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_pep8_test(self):
        """test pep8 for test to FileStorage class"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_module_doc(self):
        """test for the doc in module"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file without a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file without a docstring")

    def test_class_doc(self):
        """test for class documentation"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "class without docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "class without docstring")

    def test_func_doc(self):
        """test for doc in methods"""
        for func in self.fs_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} docstring in method".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} docstring needed in method".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """test for FileStorage class"""

    def test_all(self):
        """test for all return the __object attr"""
        strg = FileStorage()
        new_dict = strg.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, strg._FileStorage__objects)

    def test_new(self):
        """test the new add a object"""
        strg = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                strg.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, strg._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test to save object in file.json"""
        os.remove("file.json")
        strg = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        strg.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            jf = f.read()
        self.assertEqual(json.loads(string), json.loads(jf))
