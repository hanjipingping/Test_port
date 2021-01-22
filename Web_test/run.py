import unittest
from unittestreport import TestRunner

def main():
    suite = unittest.defaultTestLoader.discover(r"/Users/hanjiping/PycharmProjects/Web_test")
    runner = TestRunner(suite)
    runner.run()


if __name__ == "__main__":
    main()
