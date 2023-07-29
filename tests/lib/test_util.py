import unittest

from src.lib.util import Util

class TestUtil(unittest.TestCase):

    # -------------------
    # is_list_of_str
    # -------------------

    # Positive

    def test_is_list_of_str_arg_string_ascii(self):
        args = ['word', 'word', 'random']
        actual = Util.is_list_of_str(args)

        self.assertTrue(actual)

    def test_is_list_of_str_arg_string_utf_8_list(self):
        args = ['word', 'wórd', 'randóm']
        actual = Util.is_list_of_str(args)

        self.assertFalse(actual)

    def test_is_ascii_arg_string_utf_8(self):
        args = 'some random text?£)($*")'
        actual = Util.is_list_of_str(args)

        self.assertFalse(actual)

    def test_is_ascii_arg_string_int(self):
        args = 324532532
        actual = Util.is_list_of_str(args)

        self.assertFalse(actual)

    def test_is_ascii_arg_string_none(self):
        args = None
        actual = Util.is_list_of_str(args)

        self.assertFalse(actual)

    # Negative

    def test_is_ascii_arg_empty(self):
        with self.assertRaises(Exception) as context:
            Util.is_list_of_str()
        self.assertIn('missing 1 required positional argument', str(context.exception))