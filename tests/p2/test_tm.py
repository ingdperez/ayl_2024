import os
import unittest
import json
from p2.tm import turing_machine


class TestCaseE6(unittest.TestCase):

    def test_sum(self):
        with open("sum.json", 'r') as data:
            tm = json.load(data)
            v = [
                ("###0000###", True, "###0001###"),
                ("###0011###", True, "###0100###"),
                ("###0010###", True, "###0011###"),
                ("###1111###", True, "##10000###"),
                ("###1###", True, "##10###"),
                ("###0###", True, "###1###")
            ]
            for t in v:
                with self.subTest(t[0]):
                    r = turing_machine(tm, t[0])
                    self.assertEqual((r[0], r[1].replace("#", "")), (t[1], t[2].replace("#", "")))

    def test_0n1m(self):
        with open("0n1m.json", 'r') as data:
            tm = json.load(data)
            v = [("###01###", True),
                 ("###01111###", True),
                 ("###011011###", False),
                 ("###00001###", True),
                 ("###000010###", False),
                 ("###0###", False),
                 ("###111###", False)]
            for t in v:
                 with self.subTest(t[0]):
                  r = turing_machine(tm, t[0])
                  self.assertEqual(r[0], t[1])  # No comparó las cintas

    def test_palindromo(self):
        with open("palindromo.json", 'r') as data:
            tm = json.load(data)
            v = [
                ("###0###", True),
                ("###1###", True),
                ("###01###", False),
                ("###10###", False),
                ("###010###", True),
                ("###101###", True),
                ("###0110###", True),
                ("###1001###", True),
                ("###000111000###", True),
                ("###100010001###", True),
                ("###100011001###", False),
                ("###0011001100###", True),
                ("###0111001100###", False)
            ]
            for t in v:
                with self.subTest(t[0]):
                    r = turing_machine(tm, t[0])
                    self.assertEqual(r[0], t[1]) # No comparó las cintas


    def test_igual_cantidad_0_y_1(self):
        with open("nro_1=nro_0.json", 'r') as data:
            tm = json.load(data)
            v = [
                ("###0###", False),
                ("###1###", False),
                ("###01###", True),
                ("###10###", True),
                ("###010###", False),
                ("###101###", False),
                ("###0110###", True),
                ("###1001###", True),
                ("###000111000###", False),
                ("###100010001###", False),
                ("###100011001###", False),
                ("###0011001100###", False),
                ("###0111001100###", True),
                ("###0101010101010101###", True),
                ("###1010101010101010###", True),
                ("###0101010101010010###", False)
            ]
            for t in v:
                with self.subTest(t[0]):
                    r = turing_machine(tm, t[0])
                    self.assertEqual(r[0], t[1])  # No comparó las cintas


if __name__ == '__main__':
    unittest.main()