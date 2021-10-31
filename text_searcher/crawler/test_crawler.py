import unittest
from crawler import get_files

class TestCrawler(unittest.TestCase):

    def test_basic(self): #must start with test_
        basepath = "." 
        ls = list(get_files(basepath))
        for file in ls:
            self.assertIn(str(file),[".gitignore","LICENSE","README.md"])


if __name__ == "__main__":
    unittest.main()