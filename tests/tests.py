import unittest

class TestTitle(unittest.TestCase):
    def test_title_overline():
        title_string = "==\nAAAAA\n=="
        self.assertFalse(check_title_overline(title_string=title_string))

if __name__ == '__main__':
    unittest.main()
