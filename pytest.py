import unittest

class Test(unittest.TestCase):

    def test_helloWorld(self):
        message = "Hello World"
        self.assertEqual("Hello World", message)

if __name__ == "__main__":
	unittest.main()