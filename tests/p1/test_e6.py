import unittest

from p1.e6 import validate_a, validate_b, validate_c, validate_d, validate_e, validate_f, validate_g


class TestCaseE6(unittest.TestCase):
    def test_e6_a(self):
        v = [("20", True), ("-344", True), ("-02", True), ("2", True), ("0", True), ("00344", True), ("1", False),
             ("-1", False), ("-000001", False)]
        for t in v:
            with self.subTest(t[0]):
                self.assertEqual(t[1], validate_a(t[0]))

    def test_e6_b(self):
        v = [("20", True), ("-344", True), ("-02", False), ("2", True), ("0", True), ("00344", False), ("1", False), ("-1", False), ("-000001", False)]
        for t in v:
            with self.subTest(t[0]):
                self.assertEqual(t[1], validate_b(t[0]))

    def test_e6_c(self):
        v = [("foo", True), ("_foo", True), ("_0foo_______FOO", True), ("_____Foo_______FOO", True), ("0foo", False), ("-0foo", False), ("foo-bar-baz", False)]
        for t in v:
            with self.subTest(t[0]):
                self.assertEqual(t[1], validate_c(t[0]))

    def test_e6_d(self):
        v = [("aaaabccccc", True), ("abbbbc", False), ("caaab", False), ("abc", True), ("abccccccccccc", True), ("aaaaaaaaaaaaabc", True), ("ac", False), ("", False)]
        for t in v:
            with self.subTest(t[0]):
                self.assertEqual(t[1], validate_d(t[0]))

    def test_e6_e(self):
        v = [("", False), ("127.0.0.1", True), ("0.0.0.0", True), ("255.255.255.255", True), ("10.20.30.40", True), ("10.256.30.40", False), ("10.20.030.40", False), ("127.0.1", False), ("127.0.0.0.1", False), ("..255.255", False), (" 127.0.0.1", False), ("127.0.0.1 ", False), (" 127.0.0.1 ", False)]
        for t in v:
            with self.subTest(t[0]):
                self.assertEqual(t[1], validate_e(t[0]))


    def test_e6_f(self):
        v = [("", False),
             ("127.0.0.1:", False),
             ("127.0.0.1:80", True),
             ("127.0.0.1:65535", True),
             ("0.0.0.0", True),
             ("0.0.0.0:65536", False),
             ("255.255.255.255", True),
             ("10.20.30.40", True),
             ("10.256.30.40", False),
             ("10.20.030.40", False),
             ("127.0.1", False),
             ("127.0.1:8080", False),
             ("127.0.0.0.1", False),
             ("..255.255", False),
             (" 127.0.0.1", False),
             ("127.0.0.1 ", False),
             (" 127.0.0.1 ", False)]
        for t in v:
            with self.subTest(t[0]):
                self.assertEqual(t[1], validate_f(t[0]))

    def test_e6_g(self):
        v = [("412458596800791", False), ("4124585968007917", True), ("4074442565742969", True), ("4080649537159229", True), ("3080649537159229", False), ("4404918027486", True), ("1111335754105", False)]
        for t in v:
            with self.subTest(t[0]):
                self.assertEqual(t[1], validate_g(t[0]))


if __name__ == '__main__':
    unittest.main()
