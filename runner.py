import run as r
from selenium import webdriver
import unittest

unittest.TestLoader.sortTestMethodsUsing = None

class testRunner(unittest.TestCase): 

    driver = webdriver.Edge()

    def test1(self):
        r.testPythonSelenium(self.driver)
        return True

    if __name__ == "__main__":
        unittest.main()