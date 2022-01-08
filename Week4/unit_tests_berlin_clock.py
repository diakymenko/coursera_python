import unittest

from Coursera_Python.Week4 import Berlin_clock


class BerlinClockTestCase(unittest.TestCase):

    clock = Berlin_clock

    def test_upper_case_word(self):
        self.assertEqual(self.clock.upper_case("hello"), "HELLO")

    def test_upper_case_space(self):
        self.assertEqual(self.clock.upper_case("abcd efg"), "ABCD EFG")

    def test_upper_case_capital(self):
        self.assertEqual(self.clock.upper_case("Abcd eFg"), "ABCD EFG")

    def test_upper_case_blank(self):
        self.assertEqual(self.clock.upper_case(""), "")

    def test_to_berlin_clock_time(self):
        self.assertEqual(self.clock.to_berlin_clock_time("00:00:00"),"Y OOOO OOOO OOOOOOOOOOO OOOO")
        self.assertEqual(self.clock.to_berlin_clock_time("00:00:01"), "O OOOO OOOO OOOOOOOOOOO OOOO")

        self.assertEqual(self.clock.to_berlin_clock_time("09:00:56"), "Y ROOO RRRR OOOOOOOOOOO OOOO")
        self.assertEqual(self.clock.to_berlin_clock_time("13:00:01"),"O RROO RRRO OOOOOOOOOOO OOOO")

        self.assertEqual(self.clock.to_berlin_clock_time("17:17:18"), "Y RRRO RROO YYROOOOOOOO YYOO")
        self.assertEqual(self.clock.to_berlin_clock_time("23:59:59"),"O RRRR RRRO YYRYYRYYRYY YYYY")

        #self.assertEqual(self.clock.to_berlin_clock_time("99:99:99"),"O RRRR RRRO YYRYYRYYRYY YYYY")
        #self.assertEqual(self.clock.to_berlin_clock_time("ssd"), "O RRRR RRRO YYRYYRYYRYY YYYY")





if __name__ == '__main__':
    unittest.main()