#!/usr/bin/python3
"""
Module thats contain unittest for the consol
"""

import console
import inspect
import pep8
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def tets_create(self):

    def test_help_help(self):

    def test_prompt(self):

    def test_emptyline(self):

    def test_quit(self):

    def test_create_notation(self):

    def test_show(self):

    def test_show_notation(self):

    def test_destroy(self):

    def test_destroy_notation(self):

    def test_all(self):

    def test_all_notation(self):

    def test_update(self):

    def test_update_notation(self):

    def test_count(self):
