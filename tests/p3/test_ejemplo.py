import unittest

from p3.Parser import Parser


class TestCaseParser(unittest.TestCase):
    def test_exception(self):
        word = "001011$"
        p = Parser()
        self.assertRaises(Exception, p.evaluate, word)

    def test_1(self):
        word = "1$"
        p = Parser()
        self.assertRaises(Exception, p.evaluate, word)

    def test_00111(self):
        word = "00111$"
        p = Parser()
        self.assertFalse(p.evaluate(word))

    def test_01(self):
        word = "01$"
        p = Parser()
        self.assertTrue(p.evaluate(word))

    def test_0011(self):
        word = "0011$"
        p = Parser()
        self.assertTrue(p.evaluate(word))

    def test_10(self):
        word = "10$"
        p = Parser()
        self.assertRaises(Exception, p.evaluate, word)


if __name__ == '__main__':
    unittest.main()
