import rst2rst2
import unittest


class TestTitle(unittest.TestCase):
    def test_title_overline():
        title_string = "==\nAAAAA\n=="
        self.assertFalse(rst2rst2.check_title_overline(title_string=title_string))


if __name__ == "__main__":
    unittest.main()
